from pydantic import BaseModel, Field

class ResumeUploadRequest(BaseModel):
    file: bytes = Field(..., description="The resume file in binary format")
    filename: str = Field(..., description = "The namo of the file being uploades")
    