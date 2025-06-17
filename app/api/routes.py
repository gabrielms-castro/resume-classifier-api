from fastapi import FastAPI, HTTPException, UploadFile, File, status

from app.db.mongo import save
from app.models.resume import ResumeUploadRequest
from app.services.classifier import classify_resume
from app.services.text_extractor import call_text_extractor


app = FastAPI()

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
        return HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsuported file type: {file_type}. Supported types are: {', '.join(extensions)}"
        )
    
    contents = await file.read()
    if len(contents) == 0:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"error: File is empty or could not be processed. File size: {len(contents)} bytes",
        )
        
    text = call_text_extractor(contents, file_type)
        
    (label, score) = classify_resume(text)
    
    document = {
        "filename": file.filename,
        "file_size": len(contents),
        "file_type": file.content_type,
        "classification": {
            "label": label,
            "confidence_score": score
        }
    }
    
    data = ResumeUploadRequest(
        file=contents,
        filename=file.filename
    )
    
    _id = save(document)
    
    return {
        "id": _id,
        "filename": file.filename,
        "classification": {
            "label": label,
            "confidence_score": score
        }
    }
