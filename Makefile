run-server:
	@uvicorn app.api.routes:app --reload