import streamlit as st
import requests
# from app.controller.api_client.call_api import call_resume_analyzer
# TODO se for rodar local, não precisa da API (ou precisa?)


def call_resume_analyzer(job_description, resume):
    if (resume is None 
        or not job_description
    ):
        raise Exception("Invalid Resume of Job Description")
    
    file = {"file": (resume.name, resume.getvalue(), resume.type)}
    data = {"job_description": job_description}
    
    response = requests.post(
        "http://localhost:8000/upload_resume/",
        files=file,
        data=data
    )
    
    return response
    
st.title("Resume Analyzer API")

job_description = st.text_input("## InsertJob Description")
resume = st.file_uploader("Resume")
analyze_resume_btn = st.button("Analyze Resume and Job", use_container_width =True)

if analyze_resume_btn:
    try:
        response = call_resume_analyzer(job_description=job_description, resume=resume)
        if response.status_code == 200:
            result = response.json()["classification"]
            st.success("Success!")
            st.write("#### Result: ", result["label"])
            st.write("#### Resume Score: ", int(result["score"]))
            st.write("#### Tip:\n", result["ai_tip"])
            
            st.write("#### Gaps:")
            col1, col2 = st.columns([0.1,0.9])
            for i, gap in enumerate(result['key_gaps']):
                with col1:
                    col1.write(f"{i + 1}.")
                with col2:
                    col2.write(gap)
                    
            st.write("#### Strengths")
            col1, col2 = st.columns([0.1,0.9])
            for i, strength in enumerate(result['strengths']):
                with col1:
                    col1.write(f"{i + 1}.")
                with col2:
                    col2.write(strength)
    except Exception as exc:
        st.error(exc)
    

    

