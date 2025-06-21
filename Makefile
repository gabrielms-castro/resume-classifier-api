startup:
	docker compose up -d && uvicorn main:app --reload

docker-up:
	docker compose up -d
	
docker-down:
	docker compose down