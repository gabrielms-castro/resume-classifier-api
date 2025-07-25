from app.models.resume_schemas import ClassificationDict
from .config import (
    MAX_CHARS,
    MODEL_NAME,
    SYSTEM_PROMPT,
    GEMINI_API_KEY
)

from langchain_google_genai import ChatGoogleGenerativeAI




def ai_resume_analyze(resume: str, job_description: str) -> ClassificationDict:
    # TODO - inserir os itens abaixo no schemas para melhorar resultado
    
    # TODO - o resultado da IA ainda está muito paparicador. Testei uma vaga de senior para golang e java 
    # e ele me deu 75 de nota, sendo que nem tenho essas skills no curriculo
    
    prompt = f"""
    You are an expert HR recruiter and career coach. Analyze the resume against the job description with a critical eye.

    **Task**: Evaluate how well the candidate matches the role and provide actionable improvement advice.

    **Resume**:
    {resume}

    **Job Description**:
    {job_description}

    **Instructions**:
    1. Compare skills, experience, and qualifications critically
    2. Identify specific gaps and strengths
    3. Provide concrete, actionable improvement tips
    4. Be honest but constructive in your assessment
    5. For key gaps, make sure that you use negative words so the user don't get confused

    **Required JSON Output**:
    {{
        "label": "Strong Match | Good Match | Match | Poor Match | No Match",
        "score": <integer 0-100>,
        "ai_tip": "<specific, actionable advice in 3-5 sentences>",
        "key_gaps": list["<gap1>", "<gap2>", "<gap3>"] max. 3,
        "strengths": list["<strength1>", "<strength2>"] max. 3   

    }}

    **Response Language**: Match the job description's language.
    **Tone**: Professional, direct, and constructive.
    """
    
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        max_tokens=MAX_CHARS,
        temperature=0.1,
        api_key=GEMINI_API_KEY
    )
    
    structured_llm = llm.with_structured_output(ClassificationDict)
    return structured_llm.invoke(prompt)
    
    