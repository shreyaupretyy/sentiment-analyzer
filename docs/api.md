# API Documentation

The Sentiment Analyzer provides a simple REST API for analyzing text sentiment.

## Endpoints

### POST /api/v1/analyze

Analyzes the sentiment of provided text.

**Request Body**:

```json
{
  "text": "I love this amazing product!"
}
```

**Response**:

```json
{
  "text": "I love this amazing product!",
  "sentiment": "positive",
  "confidence": 0.85
}
```

#### Request Fields

| Field | Type   | Description              | Required |
|-------|--------|--------------------------|----------|
| text  | string | The text to analyze      | Yes      |

#### Response Fields

| Field      | Type   | Description                               |
|------------|--------|-------------------------------------------|
| text       | string | The original text that was analyzed       |
| sentiment  | string | The detected sentiment (positive, negative, neutral) |
| confidence | float  | Confidence score (0-1) of the sentiment detection |

#### Status Codes

| Status Code | Description |
|-------------|-------------|
| 200         | Success     |
| 422         | Validation Error (invalid request body) |
| 500         | Server Error |

### GET /health

Health check endpoint for monitoring.

**Response**:

```json
{
  "status": "healthy"
}
```

## How the Sentiment Analysis Works

The sentiment analyzer uses a rule-based approach with predefined word lists:

1. Text is preprocessed and tokenized into words
2. Words are matched against positive and negative word lists
3. Negation words (like "not") are detected and flip the sentiment
4. The final sentiment is determined by the predominance of positive or negative words
5. Confidence is calculated based on the ratio of positive/negative words