from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Review(Base):
    """
    SQLAlchemy model for product reviews
    Stores review text, sentiment analysis results, and key points from AI
    """
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    review_text = Column(Text, nullable=False)
    sentiment = Column(String(50))  # positive, negative, neutral
    confidence_score = Column(Float)
    key_points = Column(Text)  # JSON string from Gemini
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert model instance to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'review_text': self.review_text,
            'sentiment': self.sentiment,
            'confidence_score': self.confidence_score,
            'key_points': self.key_points,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
