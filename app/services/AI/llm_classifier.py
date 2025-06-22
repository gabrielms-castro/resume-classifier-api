from app.models.resume_schemas import ClassificationDict
from .config import (
    MAX_CHARS,
    MODEL_NAME,
    SYSTEM_PROMPT,
    GEMINI_API_KEY
)

from langchain_google_genai import ChatGoogleGenerativeAI




def ai_resume_analyze(resume: str, job_description: str) -> ClassificationDict:
    prompt = f"""
    Analyze the following resume and job description. 
    Return a JSON with: 'label', 'score', and 'ai_tip'.
    
    Resume:
    {resume}
    
    Job Description:
    {job_description}    
    """
    
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        max_tokens=MAX_CHARS,
        temperature=0.1,
        api_key=GEMINI_API_KEY
    )
    
    structured_llm = llm.with_structured_output(ClassificationDict)
    return structured_llm.invoke(prompt)
    
    