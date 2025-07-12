#!/bin/bash
docker compose up -d
source venv/bin/activate
streamlit run app/view/streamlit.py
uvicorn app.api.routes:app --reload
docker compose down