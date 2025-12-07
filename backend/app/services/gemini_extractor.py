import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

class GeminiExtractor:
    """
    Key points extraction service using Google Gemini AI
    Extracts key points in the same language as the input text
    Uses the latest Gemini API (v1beta)
    """
    
    def __init__(self):
        # Support both GEMINI_API_KEY (recommended) and GEMINI_API_TOKEN (legacy)
        self.api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GEMINI_API_TOKEN') or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key not found. Please set GEMINI_API_KEY or GEMINI_API_TOKEN in .env file")
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize Gemini AI model"""
        try:
            genai.configure(api_key=self.api_key)
            # Using gemini-2.5-flash (latest stable model)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            print("✅ Gemini extractor initialized successfully with gemini-2.5-flash")
        except Exception as e:
            print(f"❌ Error initializing Gemini: {str(e)}")
            print("💡 Tip: Make sure your GEMINI_API_KEY is valid and has access to Gemini API")
            raise
    
    def extract_key_points(self, review_text):
        """
        Extract key points from review text
        
        Args:
            review_text (str): Review text to analyze
            
        Returns:
            str: JSON string containing array of key points
        """
        if not review_text or not review_text.strip():
            raise ValueError("Review text cannot be empty")
        
        try:
            # Create prompt that instructs Gemini to respond in same language
            prompt = f"""
Analyze the following product review and extract the key points.
IMPORTANT: Respond in the SAME language as the review text below.

Review: {review_text}

Extract 3-5 key points from this review. Return ONLY a JSON array of strings, nothing else.
Example format: ["point 1", "point 2", "point 3"]

If the review is in Indonesian, respond in Indonesian.
If the review is in English, respond in English.
Keep each point concise (1-2 sentences maximum).
"""
            
            # Generate response using Gemini
            response = self.model.generate_content(prompt)
            
            # Extract text from response
            key_points_text = response.text.strip()
            
            # Try to parse as JSON to validate
            try:
                # Remove markdown code blocks if present
                if key_points_text.startswith('```'):
                    # Remove code fence
                    parts = key_points_text.split('```')
                    if len(parts) >= 2:
                        key_points_text = parts[1]
                        # Remove 'json' language identifier if present
                        if key_points_text.startswith('json'):
                            key_points_text = key_points_text[4:]
                        key_points_text = key_points_text.strip()
                
                # Validate JSON
                parsed = json.loads(key_points_text)
                if not isinstance(parsed, list):
                    raise ValueError("Response is not a JSON array")
                
                # Ensure we have 3-5 points
                if len(parsed) > 5:
                    parsed = parsed[:5]
                
                return json.dumps(parsed, ensure_ascii=False)
            except json.JSONDecodeError as e:
                # If parsing fails, return as simple array
                print(f"⚠️ Warning: Could not parse Gemini response as JSON: {key_points_text}")
                print(f"   JSON Error: {str(e)}")
                # Fallback: return the text as a single point
                return json.dumps([key_points_text], ensure_ascii=False)
                
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Error extracting key points: {error_msg}")
            
            # Provide helpful error messages
            if "404" in error_msg:
                print("💡 Tip: Model not found. Try updating to a supported model.")
            elif "API key" in error_msg.lower():
                print("💡 Tip: Check your GEMINI_API_KEY in the .env file")
            elif "quota" in error_msg.lower():
                print("💡 Tip: You may have exceeded your API quota. Check Google AI Studio.")
            
            raise

# Global instance
gemini_extractor = GeminiExtractor()

