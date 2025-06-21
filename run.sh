#!/bin/bash
docker compose up -d
uvicorn main:app --reload
docker compose down