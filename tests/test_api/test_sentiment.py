
class TestSentimentEndpoint:
    """Tests for the sentiment analysis API endpoint."""

    def test_analyze_positive(self, client):
        """Test analyzing positive text."""
        response = client.post(
            "/api/v1/analyze",
            json={"text": "I love this amazing product!"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "positive"
        assert data["confidence"] > 0

    def test_analyze_negative(self, client):
        """Test analyzing negative text."""
        response = client.post(
            "/api/v1/analyze",
            json={"text": "This is terrible, I hate it."}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "negative"
        assert data["confidence"] > 0

    def test_analyze_neutral(self, client):
        """Test analyzing neutral text."""
        response = client.post(
            "/api/v1/analyze",
            json={"text": "This is a regular statement."}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "neutral"

    def test_invalid_request(self, client):
        """Test sending an invalid request."""
        response = client.post(
            "/api/v1/analyze",
            json={"invalid_field": "This should fail"}
        )

        assert response.status_code == 422  # Validation error

    def test_empty_text(self, client):
        """Test sending empty text."""
        response = client.post(
            "/api/v1/analyze",
            json={"text": ""}
        )

        assert response.status_code == 422  # Validation error for min_length=1

    def test_health_endpoint(self, client):
        """Test the health check endpoint."""
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
