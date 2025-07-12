import streamlit as st
import requests

# TODO se for rodar local, não precisa da API (ou precisa?)
def call_resume_analyzer(job_description, resume):
    if resume is not None and job_description:
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
    response = call_resume_analyzer(job_description=job_description, resume=resume)
    if response.status_code == 200:
        result = response.json()["classification"]
        st.success("Success!")
        st.write("#### Result: ", result["label"])
        st.write("#### Resume Score: ", result["score"])
        st.write("#### Tip:\n", result["ai_tip"])

