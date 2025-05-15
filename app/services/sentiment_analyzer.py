import logging
from typing import Dict, List, Tuple

from app.models.sentiment import SentimentType

logger = logging.getLogger(__name__)


class SentimentAnalyzer:
    """A simple rule-based sentiment analyzer."""
    
    def __init__(self):
        # Simple word lists for sentiment detection
        self.positive_words = {
            "good", "great", "excellent", "awesome", "amazing", "love", "happy",
            "joy", "fantastic", "wonderful", "beautiful", "brilliant", "enjoy",
            "glad", "positive", "nice", "perfect", "better", "best", "win",
            "success", "successful"
        }
        
        self.negative_words = {
            "bad", "terrible", "awful", "horrible", "hate", "sad", "angry",
            "poor", "disappointing", "negative", "ugly", "worst", "worse",
            "fail", "failure", "problem", "issue", "difficult", "unhappy",
            "annoying"
        }
        
        # Negation words (can flip sentiment)
        self.negation_words = {
            "not", "no", "never", "don't", "doesn't", "didn't", "cannot",
            "can't", "won't", "wouldn't", "shouldn't", "isn't", "aren't",
            "wasn't", "weren't", "haven't", "hasn't", "hadn't", "nor", "neither"
        }
    
    def analyze(self, text: str) -> Tuple[SentimentType, float]:
        """
        Analyze text for sentiment and return sentiment type with confidence.
        
        Args:
            text: The text to analyze
        
        Returns:
            Tuple of (sentiment_type, confidence_score)
        """
        if not text:
            logger.warning("Empty text provided for sentiment analysis")
            return SentimentType.NEUTRAL, 0.5
        
        # Preprocess text
        text = text.lower()
        words = text.split()
        
        # Count sentiments and handle negations
        sentiment_scores = self._count_sentiment_words(words)
        positive_score = sentiment_scores["positive"]
        negative_score = sentiment_scores["negative"]
        total_score = positive_score + negative_score
        
        # Determine sentiment
        if total_score == 0:
            logger.info("No sentiment words found, classifying as neutral")
            return SentimentType.NEUTRAL, 0.5
        
        if positive_score > negative_score:
            confidence = positive_score / total_score
            return SentimentType.POSITIVE, confidence
        elif negative_score > positive_score:
            confidence = negative_score / total_score
            return SentimentType.NEGATIVE, confidence
        else:
            return SentimentType.NEUTRAL, 0.5
    
    def _count_sentiment_words(self, words: List[str]) -> Dict[str, int]:
        """
        Count positive and negative words with negation handling.
        
        Args:
            words: List of words from the text
            
        Returns:
            Dictionary with counts of positive and negative sentiment
        """
        positive_count = 0
        negative_count = 0
        negation_active = False
        
        for i, word in enumerate(words):
            # Check for negation
            if word in self.negation_words:
                negation_active = True
                continue
            
            # Reset negation after 3 words
            if i > 0 and i % 3 == 0:
                negation_active = False
            
            # Count sentiment words
            if word in self.positive_words:
                if negation_active:
                    negative_count += 1
                else:
                    positive_count += 1
            
            if word in self.negative_words:
                if negation_active:
                    positive_count += 1
                else:
                    negative_count += 1
        
        return {
            "positive": positive_count,
            "negative": negative_count
        }