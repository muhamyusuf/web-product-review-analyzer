from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()

class SentimentAnalyzer:
    """
    Sentiment analysis service using Hugging Face Transformers
    Model: cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual
    Supports multiple languages including Indonesian and English
    """
    
    def __init__(self):
        # Using multilingual model that supports Indonesian
        self.model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual"
        self.token = os.getenv('HUGGINGFACE_ACCESS_TOKEN')
        self.analyzer = None
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the sentiment analysis pipeline"""
        try:
            self.analyzer = pipeline(
                "sentiment-analysis",
                model=self.model_name,
                token=self.token
            )
            print(f"✅ Sentiment analyzer initialized with multilingual model (supports Indonesian & English)")
        except Exception as e:
            print(f"❌ Error initializing sentiment analyzer: {str(e)}")
            raise
    
    def analyze(self, text):
        """
        Analyze sentiment of given text
        
        Args:
            text (str): Text to analyze (supports multiple languages)
            
        Returns:
            dict: {
                'sentiment': 'positive' | 'negative' | 'neutral',
                'confidence': float (0-1)
            }
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        try:
            result = self.analyzer(text[:512])[0]  # Limit to 512 tokens
            
            # Map result to our format
            label = result['label'].lower()
            confidence = result['score']
            
            # XLM-RoBERTa returns: negative, neutral, positive
            sentiment_map = {
                'positive': 'positive',
                'negative': 'negative',
                'neutral': 'neutral',
                'pos': 'positive',
                'neg': 'negative',
                'neu': 'neutral'
            }
            
            sentiment = sentiment_map.get(label, 'neutral')
            
            return {
                'sentiment': sentiment,
                'confidence': round(confidence, 4)
            }
        except Exception as e:
            print(f"❌ Error analyzing sentiment: {str(e)}")
            raise

# Global instance
sentiment_analyzer = SentimentAnalyzer()

