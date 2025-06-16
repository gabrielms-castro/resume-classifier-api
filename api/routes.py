from fastapi import FastAPI, UploadFile, File
from models.resume import ResumeUploadRequest


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Resume Classifier API"}

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    
    data = ResumeUploadRequest(
        file=contents,
        filename=file.filename
    )
    
    return {
        "filename": data.filename,
        "file_size": len(data.file),
        "file_type": file.content_type
    }