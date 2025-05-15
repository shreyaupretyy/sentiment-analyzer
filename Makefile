.PHONY: setup install lint format test test-cov clean build run docker-build docker-run docs help

setup: ## Set up development environment
	python -m venv venv
	@echo "Run 'source venv/bin/activate' to activate the virtual environment"

install: ## Install dependencies
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

lint: ## Run linters
	flake8 app tests
	black --check app tests
	isort --check-only --profile black app tests

format: ## Format code
	isort --profile black app tests
	black app tests

test: ## Run tests
	pytest -v

test-cov: ## Run tests with coverage
	pytest --cov=app --cov-report=term --cov-report=html

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +

build: ## Build the package
	python -m pip install --upgrade pip
	pip install build
	python -m build

run: ## Run the application
	uvicorn app.main:app --reload

docker-build: ## Build Docker image
	docker build -t sentiment-analyzer:latest .

docker-run: ## Run Docker container
	docker run -p 8000:8000 --env-file .env sentiment-analyzer:latest

docs: ## Build documentation
	mkdocs build

docs-serve: ## Serve documentation locally
	mkdocs serve

help: ## Show help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help