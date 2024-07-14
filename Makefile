install:
	poetry install
dev:
	poetry run flask --app page_analyzer:app run
lint:
	poetry run flake8 page_analyzer

.PHONY: install dev lint