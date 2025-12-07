"""
Test script for Product Review Analyzer API
Run this to verify backend is working correctly
"""

import requests
import json

BASE_URL = "http://localhost:6543/api"

def test_health_check():
    """Test health check endpoint"""
    print("🔍 Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check PASSED")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Health check FAILED: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check ERROR: {str(e)}")
        return False

def test_analyze_review():
    """Test analyze review endpoint"""
    print("\n🔍 Testing analyze review...")
    
    test_reviews = [
        {
            "text": "This product is amazing! Great quality and fast shipping.",
            "expected_sentiment": "positive"
        },
        {
            "text": "Terrible product. Waste of money. Very disappointed.",
            "expected_sentiment": "negative"
        },
        {
            "text": "Produk ini bagus sekali! Kualitas mantap dan pengiriman cepat.",
            "expected_sentiment": "positive"
        }
    ]
    
    for i, review in enumerate(test_reviews, 1):
        print(f"\n  Test {i}: {review['text'][:50]}...")
        try:
            response = requests.post(
                f"{BASE_URL}/analyze-review",
                json={"review_text": review['text']},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 201:
                data = response.json()
                if data.get('status') == 'success':
                    result = data['data']
                    sentiment = result.get('sentiment', '').lower()
                    confidence = result.get('confidence_score', 0)
                    
                    print(f"  ✅ Analysis PASSED")
                    print(f"     Sentiment: {sentiment} (confidence: {confidence:.2%})")
                    print(f"     Key Points: {result.get('key_points', '[]')[:100]}...")
                    
                    # Verify expected sentiment
                    if sentiment == review['expected_sentiment']:
                        print(f"  ✅ Sentiment matches expected: {review['expected_sentiment']}")
                    else:
                        print(f"  ⚠️ Sentiment mismatch: got {sentiment}, expected {review['expected_sentiment']}")
                else:
                    print(f"  ❌ Analysis FAILED: {data}")
            else:
                print(f"  ❌ Analysis FAILED: Status {response.status_code}")
                print(f"     Response: {response.text}")
        except Exception as e:
            print(f"  ❌ Analysis ERROR: {str(e)}")

def test_get_reviews():
    """Test get reviews endpoint"""
    print("\n🔍 Testing get reviews...")
    try:
        response = requests.get(f"{BASE_URL}/reviews?page=1&limit=5")
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                reviews_data = data['data']
                print(f"✅ Get reviews PASSED")
                print(f"   Total reviews: {reviews_data.get('total', 0)}")
                print(f"   Page: {reviews_data.get('page', 1)}/{reviews_data.get('total_pages', 0)}")
                print(f"   Reviews fetched: {len(reviews_data.get('reviews', []))}")
                return True
            else:
                print(f"❌ Get reviews FAILED: {data}")
                return False
        else:
            print(f"❌ Get reviews FAILED: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Get reviews ERROR: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🧪 Product Review Analyzer API - Test Suite")
    print("=" * 60)
    print(f"📡 Testing API at: {BASE_URL}")
    print("=" * 60)
    
    # Run tests
    health_ok = test_health_check()
    
    if health_ok:
        test_analyze_review()
        test_get_reviews()
    else:
        print("\n❌ Health check failed. Please ensure backend is running.")
        print("   Run: pserve development.ini")
    
    print("\n" + "=" * 60)
    print("✅ Test suite completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
