from typing import Dict, List
from pydantic import BaseModel, Field
from typing_extensions import Annotated, TypedDict


class ClassificationDict(TypedDict):
    label: Annotated[str, ..., "If the resume was classified, this should contain the label of the classification (e.g., 'Strong Match', 'Good Match', 'Match', 'Poor Match', 'No Match')"]
    score: Annotated[int, ..., "Give the resume a score based on the job description and the resume content. The score should be between 0 and 100, where 100 is a perfect match and 0 is no match at all."]
    ai_tip: Annotated[str, ..., "Provide a tip or suggestion based on the classification result. This could be a recommendation for improving the resume or advice on how to better match the job description."]
    key_gaps: Annotated[List[str], "List of missing skills, experiences, or qualifications identified in the resume. Make sure to be negative"]
    strengths: Annotated[List[str], "List of candidate's key strengths and qualifications that match the job requirements"]  
    
class ResumeUploadRequest(BaseModel):
    file: bytes = Field(..., description="The resume file in binary format")
    file_content: str = Field(..., description="The processed text content of the resume")
    filename: str = Field(..., description = "The namo of the file being uploades")
    file_size: int = Field(..., description="The size of the file in bytes")
    file_type: str = Field(..., description="The MIME type of the file")
    job_description: str = Field(..., description="The job description to compare against the resume")
    classification: ClassificationDict = Field(
        ..., 
        description="Classification result including label and confidence score"
    )
