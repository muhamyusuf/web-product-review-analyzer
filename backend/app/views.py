from pyramid.view import view_config
from pyramid.response import Response
import json
from sqlalchemy import desc
from .models import Review
from .database import get_db_session
from .services.sentiment_analyzer import sentiment_analyzer
from .services.gemini_extractor import gemini_extractor

@view_config(route_name='analyze_review', renderer='json', request_method='POST')
def analyze_review(request):
    """
    POST /api/analyze-review
    Analyze a product review using AI services
    
    Request Body:
        {
            "review_text": "string"
        }
    
    Returns:
        {
            "id": int,
            "review_text": string,
            "sentiment": string,
            "confidence_score": float,
            "key_points": string (JSON array),
            "created_at": string (ISO format)
        }
    """
    try:
        # Parse request body
        data = request.json_body
        review_text = data.get('review_text', '').strip()
        
        # Validate input
        if not review_text:
            request.response.status = 400
            return {
                'error': 'review_text is required and cannot be empty',
                'status': 'error'
            }
        
        # Step 1: Analyze sentiment using Hugging Face
        try:
            sentiment_result = sentiment_analyzer.analyze(review_text)
            sentiment = sentiment_result['sentiment']
            confidence = sentiment_result['confidence']
        except Exception as e:
            request.response.status = 500
            return {
                'error': f'Sentiment analysis failed: {str(e)}',
                'status': 'error'
            }
        
        # Step 2: Extract key points using Gemini
        try:
            key_points = gemini_extractor.extract_key_points(review_text)
        except Exception as e:
            request.response.status = 500
            return {
                'error': f'Key points extraction failed: {str(e)}',
                'status': 'error'
            }
        
        # Step 3: Save to database
        db = get_db_session()
        try:
            review = Review(
                review_text=review_text,
                sentiment=sentiment,
                confidence_score=confidence,
                key_points=key_points
            )
            db.add(review)
            db.commit()
            
            # Get the created review with ID
            result = review.to_dict()
            
            request.response.status = 201
            return {
                'status': 'success',
                'data': result
            }
        except Exception as e:
            db.rollback()
            request.response.status = 500
            return {
                'error': f'Database error: {str(e)}',
                'status': 'error'
            }
        finally:
            db.close()
            
    except Exception as e:
        request.response.status = 500
        return {
            'error': f'Internal server error: {str(e)}',
            'status': 'error'
        }

@view_config(route_name='get_reviews', renderer='json', request_method='GET')
def get_reviews(request):
    """
    GET /api/reviews?page=1&limit=10
    Get all reviews with pagination
    
    Query Parameters:
        page: int (default: 1)
        limit: int (default: 10, max: 100)
    
    Returns:
        {
            "status": "success",
            "data": {
                "reviews": [...],
                "total": int,
                "page": int,
                "limit": int,
                "total_pages": int
            }
        }
    """
    try:
        # Get pagination parameters
        page = int(request.params.get('page', 1))
        limit = int(request.params.get('limit', 10))
        
        # Validate parameters
        if page < 1:
            page = 1
        if limit < 1 or limit > 100:
            limit = 10
        
        # Calculate offset
        offset = (page - 1) * limit
        
        # Query database
        db = get_db_session()
        try:
            # Get total count
            total = db.query(Review).count()
            
            # Get paginated reviews (ordered by newest first)
            reviews = db.query(Review)\
                .order_by(desc(Review.created_at))\
                .limit(limit)\
                .offset(offset)\
                .all()
            
            # Convert to dict
            reviews_data = [review.to_dict() for review in reviews]
            
            # Calculate total pages
            total_pages = (total + limit - 1) // limit
            
            return {
                'status': 'success',
                'data': {
                    'reviews': reviews_data,
                    'total': total,
                    'page': page,
                    'limit': limit,
                    'total_pages': total_pages
                }
            }
        finally:
            db.close()
            
    except ValueError as e:
        request.response.status = 400
        return {
            'error': 'Invalid page or limit parameter',
            'status': 'error'
        }
    except Exception as e:
        request.response.status = 500
        return {
            'error': f'Internal server error: {str(e)}',
            'status': 'error'
        }

@view_config(route_name='health', renderer='json', request_method='GET')
def health_check(request):
    """Health check endpoint"""
    return {
        'status': 'healthy',
        'service': 'Product Review Analyzer API'
    }
