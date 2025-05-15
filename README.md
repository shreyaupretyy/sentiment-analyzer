# Sentiment Analyzer

[![CI/CD Pipeline](https://github.com/shreyaupretyy/sentiment-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/shreyaupretyy/sentiment-analyzer/actions/workflows/ci.yml)
[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://shreyaupretyy.github.io/sentiment-analyzer/)

A FastAPI microservice that performs sentiment analysis on text using a rule-based approach.
Built following the 12-Factor App methodology.

[View Documentation](https://shreyaupretyy.github.io/sentiment-analyzer/)

## Features

- Simple text sentiment analysis (positive, negative, neutral)
- RESTful API with FastAPI
- Docker containerization
- Comprehensive test suite
- CI/CD with GitHub Actions

## Getting Started

### Prerequisites

- Python 3.8+
- Docker and Docker Compose (optional)

### Local Development Setup

1. **Clone the repository**

```bash
git clone https://github.com/shreyaupretyy/sentiment-analyzer.git
cd sentiment-analyzer
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

4. **Set up environment variables**

```bash
cp .env.sample .env
# Edit .env file as needed
```

5. **Install pre-commit hooks**

```bash
pre-commit install
```

6. **Run the application**

```bash
uvicorn app.main:app --reload
```

7. **Run tests**

```bash
pytest
```

### Docker Setup

1. **Build and run using Docker Compose**

```bash
docker-compose up --build
```

2. **Access the API**

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access the Swagger UI documentation at:

- `http://localhost:8000/docs` - Swagger UI
- `http://localhost:8000/redoc` - ReDoc UI

### Endpoints

- `POST /api/v1/analyze` - Analyze sentiment of text
- `GET /health` - Health check endpoint

## Environment Variables

| Variable    | Description                 | Default Value      |
| ----------- | --------------------------- | ------------------ |
| APP_NAME    | Name of the application     | sentiment-analyzer |
| APP_VERSION | Version of the application  | 0.1.0              |
| ENVIRONMENT | Deployment environment      | development        |
| HOST        | Host to bind the server to  | 0.0.0.0            |
| PORT        | Port to bind the server to  | 8000               |
| LOG_LEVEL   | Logging level               | info               |
| REDIS_HOST  | Redis host (if using Redis) | redis              |
| REDIS_PORT  | Redis port (if using Redis) | 6379               |

## Project Structure

```
sentiment-analyzer/
├── app/                # Application code
│   ├── api/            # API endpoints
│   ├── core/           # Core functionality (config, settings)
│   ├── models/         # Pydantic models
│   └── services/       # Business logic services
├── tests/              # Test suite
├── docs/               # Documentation
├── .github/            # GitHub Actions workflows
└── ...                 # Configuration files
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

- **Shreya Uprety** - [shreyaupretyy](https://github.com/shreyaupretyy)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
