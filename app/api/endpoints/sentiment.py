import logging
from fastapi import APIRouter, HTTPException

from app.models.sentiment import SentimentRequest, SentimentResponse
from app.services.sentiment_analyzer import SentimentAnalyzer

router = APIRouter()
logger = logging.getLogger(__name__)

# Initialize the sentiment analyzer
sentiment_analyzer = SentimentAnalyzer()


@router.post("/analyze", response_model=SentimentResponse, status_code=200)
async def analyze_sentiment(request: SentimentRequest):
    """
    Analyze the sentiment of the provided text.

    Returns:
        SentimentResponse: The sentiment analysis result
    """
    try:
        logger.info(f"Analyzing sentiment for text of length {len(request.text)}")

        # Perform sentiment analysis
        sentiment_type, confidence = sentiment_analyzer.analyze(request.text)

        # Return the response
        return SentimentResponse(
            text=request.text,
            sentiment=sentiment_type,
            confidence=confidence
        )

    except Exception as e:
        logger.error(f"Error analyzing sentiment: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred during sentiment analysis"
        )
