from enum import Enum

from pydantic import BaseModel, Field


class SentimentType(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text to analyze for sentiment")

    class Config:
        schema_extra = {"example": {"text": "I love this amazing product!"}}


class SentimentResponse(BaseModel):
    text: str = Field(..., description="The original text analyzed")
    sentiment: SentimentType = Field(..., description="The detected sentiment")
    confidence: float = Field(..., description="Confidence score (0-1) of sentiment detection")

    class Config:
        schema_extra = {
            "example": {
                "text": "I love this amazing product!",
                "sentiment": "positive",
                "confidence": 0.85,
            }
        }
