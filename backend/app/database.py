from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create engine
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://admin:admin123@localhost:5432/product_reviews')
engine = create_engine(DATABASE_URL, echo=False)  # Set echo=False to reduce logs

# Create session factory  
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)

def init_db():
    """Initialize database by creating all tables"""
    from .models import Base
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

def get_db_session():
    """Get database session for use in views"""
    return Session()
