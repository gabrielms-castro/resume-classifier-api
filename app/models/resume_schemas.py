from typing import Dict
from pydantic import BaseModel, Field
from typing_extensions import Annotated, TypedDict


class ClassificationDict(TypedDict):
    label: Annotated[str, ..., "If the resume was classified, this should contain the label of the classification (e.g., 'Match', 'No Match', 'Partial Match')"]
    score: Annotated[float, ..., "Give the resume a score based on the job description and the resume content. The score should be between 0 and 1, where 1 is a perfect match and 0 is no match at all."]
    ai_tip: Annotated[str, ..., "Provide a tip or suggestion based on the classification result. This could be a recommendation for improving the resume or advice on how to better match the job description."]
    
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
