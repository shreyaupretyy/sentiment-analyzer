import pytest
from app.models.sentiment import SentimentType


class TestSentimentAnalyzer:
    """Tests for the SentimentAnalyzer service."""
    
    def test_positive_sentiment(self, sentiment_analyzer):
        """Test positive sentiment detection."""
        text = "I love this product, it's really good and amazing!"
        sentiment, confidence = sentiment_analyzer.analyze(text)
        
        assert sentiment == SentimentType.POSITIVE
        assert confidence > 0.5
    
    def test_negative_sentiment(self, sentiment_analyzer):
        """Test negative sentiment detection."""
        text = "This is terrible and I hate it. Very disappointing."
        sentiment, confidence = sentiment_analyzer.analyze(text)
        
        assert sentiment == SentimentType.NEGATIVE
        assert confidence > 0.5
    
    def test_neutral_sentiment(self, sentiment_analyzer):
        """Test neutral sentiment detection."""
        text = "This is a regular statement without emotional content."
        sentiment, confidence = sentiment_analyzer.analyze(text)
        
        assert sentiment == SentimentType.NEUTRAL
        assert confidence == 0.5
    
    def test_empty_text(self, sentiment_analyzer):
        """Test handling of empty text."""
        text = ""
        sentiment, confidence = sentiment_analyzer.analyze(text)
        
        assert sentiment == SentimentType.NEUTRAL
        assert confidence == 0.5
    
    def test_negation_handling(self, sentiment_analyzer):
        """Test that negations flip sentiment properly."""
        text = "I do not like this product, it's not good."
        sentiment, confidence = sentiment_analyzer.analyze(text)
        
        assert sentiment == SentimentType.NEGATIVE
        assert confidence > 0.5