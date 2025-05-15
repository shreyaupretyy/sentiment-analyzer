import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.sentiment_analyzer import SentimentAnalyzer


@pytest.fixture
def client():
    """Create a test client for FastAPI app."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def sentiment_analyzer():
    """Create an instance of the SentimentAnalyzer for testing."""
    return SentimentAnalyzer()