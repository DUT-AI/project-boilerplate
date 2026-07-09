.PHONY: help dev-api migrate create-migration test

help:
	@echo "Available commands:"
	@echo "  make dev-api        - Start the local development server (uvicorn)"
	@echo "  make migrate        - Run all database migrations (locally using uv)"
	@echo "  make create-migration DESC=\"msg\" - Create a new migration revision (locally)"
	@echo "  make test           - Run backend test suite (locally)"

dev-api:
	cd ./backend && uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

migrate:
	cd ./backend && uv run alembic upgrade head

create-migration:
	@if [ -z "$(DESC)" ]; then echo "Error: Please specify DESC, e.g., make create-migration DESC=\"add new table\""; exit 1; fi
	cd ./backend && uv run alembic revision --autogenerate -m "$(DESC)"

test:
	cd ./backend && uv run pytest
