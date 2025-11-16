startup:
	docker compose up -d && . .venv/bin/activate && uvicorn app.api.routes:app --reload

docker-up:
	docker compose up -d
	
docker-down:
	docker compose down

ui:
	.venv/bin/python -m streamlit run app/view/streamlit.py