from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from contextlib import asynccontextmanager

from app.db.connection_options.connection import DBConnectionHandler
from app.db.repositories.resumes_repository import ResumesRepository
from app.models.resume_schemas import ResumeUploadRequest
from app.services.AI.llm_classifier import ai_resume_analyze
from app.services.text_extractor_service import call_text_extractor

db_handler = DBConnectionHandler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    global db_connection
    global resume_repository
    
    print("[DEBUG] Application startup: Initializing resources...")
    
    db_handler.connection_to_db()
    db_connection = db_handler.get_db_connection()
    resume_repository = ResumesRepository(db_connection=db_connection)
    print("[DEBUG] Database connection established:", db_connection)
    print("[DEBUG] Repository connection established:", resume_repository)
    
    yield # app running here
    
    print("[DEBUG] Application shutdown: Cleaning up resources...")
    db_handler.close_connection()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Resume Classifier API"}

@app.post("/upload_resume/", status_code=status.HTTP_200_OK)
async def upload_resume(
    job_description: str = Form(...), 
    file: UploadFile = File(...)
):
    extensions = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain"
    ]
    
    file_type = file.content_type
    if file_type not in extensions:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsuported file type: {file_type}. Supported types are: {', '.join(extensions)}"
        )
    
    content_raw = await file.read()
    if len(content_raw) == 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"error: File is empty or could not be processed. File size: {len(content_raw)} bytes",
        )
    
    if len(job_description) == 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="error: Job description cannot be empty"
        )
    
    extractor = call_text_extractor(file_type=file_type)
    content_processed = extractor.extract_text(content_raw)
    
    try:
        result = ai_resume_analyze(
            resume=content_processed,
            job_description=job_description
        )
        assert 'score' in result, "AI analysis did not return a score"
        assert 'label' in result, "AI analysis did not return a label"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI analysis failed: {str(e)}"
        )
    
    label, score, ai_tip = result.get('label'), result.get('score'), result.get('ai_tip')
    
    data = ResumeUploadRequest(
        file=content_raw,
        file_content=content_processed,
        filename=file.filename,
        file_size=len(content_raw),
        file_type=file.content_type,
        job_description=job_description,
        classification={
            "label": label,
            "score": score,
            "ai_tip": ai_tip
        }
    )
    
    document = data.model_dump()
    persist_response = resume_repository.insert_document(document)
    response = {
        "message": "Resume uploaded successfully",
        "id": str(persist_response.get("_id")),
        "filename": file.filename,
        "file_content": content_processed,
        "file_size": len(content_raw),
        "file_type": file.content_type,
        "job_description": job_description,
        "classification": {
            "label": label,
            "score": score,
            "ai_tip": ai_tip
        }      
    }
    
    return response
