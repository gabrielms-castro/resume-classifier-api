run-server:
	@uvicorn api.routes:app --reload