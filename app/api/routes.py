import subprocess
from fastapi import FastAPI, File, HTTPException, UploadFile, status
from contextlib import asynccontextmanager

# from app.db.mongo_connection import save
from app.db.connection_options.connection import DBConnectionHandler
from app.db.repositories.resumes_repository import ResumesRepository
from app.models.resume_schemas import ResumeUploadRequest
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
async def upload_resume(file: UploadFile = File(...)):
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
    
    extractor = call_text_extractor(file_type=file_type)
    content_processed = extractor.extract_text(content_raw)
    
    data = ResumeUploadRequest(
        file=content_raw,
        file_content=content_processed,
        filename=file.filename,
        file_size=len(content_raw),
        file_type=file.content_type,
        classification={
            "label": "Match",
            "score": 0.8
        }
    )
    
    document = data.model_dump()
    persist_response = resume_repository.insert_document(document)
    response = {
        "message": "Resume uploaded successfully",
        "id": str(persist_response.get("_id")),
        "filename": file.filename,
        "file_size": len(content_raw),
        "file_type": file.content_type,
        "classification": {
            "label": "Match",
            "confidence_score": 0.82
        }        
    }
    
    return response
