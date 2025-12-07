from pyramid.config import Configurator
from pyramid.renderers import JSON
from pyramid.response import Response
from .database import init_db, Session

def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    # Configure JSON renderer
    json_renderer = JSON()
    json_renderer.add_adapter(type(None), lambda obj, request: None)
    config.add_renderer('json', json_renderer)
    
    # Add CORS headers to ALL responses
    def add_cors_headers(event):
        event.response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        })
    
    config.add_subscriber(add_cors_headers, 'pyramid.events.NewResponse')
    
    # Handle OPTIONS preflight requests
    def cors_options_view(request):
        response = Response()
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        })
        return response
    
    # Add routes
    config.add_route('analyze_review', '/api/analyze-review')
    config.add_route('get_reviews', '/api/reviews')
    config.add_route('health', '/api/health')
    
    # Add OPTIONS handlers for each route
    config.add_view(cors_options_view, route_name='analyze_review', request_method='OPTIONS')
    config.add_view(cors_options_view, route_name='get_reviews', request_method='OPTIONS')
    config.add_view(cors_options_view, route_name='health', request_method='OPTIONS')
    
    # Scan for view functions
    config.scan('.views')
    
    # Initialize database
    init_db()
    
    return config.make_wsgi_app()
