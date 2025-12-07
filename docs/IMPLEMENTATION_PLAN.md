# Product Review Analyzer - Implementation Plan

## 📋 Project Overview
**Aplikasi:** Product Review Analyzer dengan AI-powered sentiment analysis  
**Tech Stack Backend:** Python 3.13 + Pyramid + SQLAlchemy + PostgreSQL + UV  
**Tech Stack Frontend:** Vite + React + Shadcn/ui + Zustand + Bun  
**Database:** PostgreSQL (postgresql://admin:admin123@localhost:5432/product_reviews)

---

## 🏗️ Project Structure

```
web-product-review-analyzer/
├── backend/
│   ├── venv/                    # UV virtual environment
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py            # SQLAlchemy models
│   │   ├── views.py             # Pyramid views/endpoints
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── sentiment_analyzer.py    # Hugging Face integration
│   │   │   └── gemini_extractor.py      # Gemini key points extraction
│   │   └── database.py          # Database configuration
│   ├── development.ini          # Pyramid configuration
│   ├── .env                     # Environment variables
│   ├── requirements.txt         # Python dependencies
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/              # Shadcn components
│   │   │   ├── ReviewForm.jsx
│   │   │   ├── ReviewResults.jsx
│   │   │   ├── ReviewHistory.jsx
│   │   │   └── ThemeToggle.jsx
│   │   ├── stores/
│   │   │   └── reviewStore.js   # Zustand state management
│   │   ├── lib/
│   │   │   └── api.js           # API client
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
└── README.md                     # Main documentation
```

---

## 📝 Implementation Steps

### **PHASE 1: Backend Setup (Python Pyramid)**

#### 1.1 Setup UV Virtual Environment
```bash
cd backend
uv venv
# Activate:
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
```

#### 1.2 Install Dependencies
Create `requirements.txt`:
```txt
pyramid==2.0.2
pyramid-tm==2.5
waitress==3.0.0
SQLAlchemy==2.0.23
psycopg2-binary==2.9.9
transformers==4.36.0
torch==2.1.0
google-generativeai==0.3.1
python-dotenv==1.0.0
pyramid-cors==0.3.0
```

Install:
```bash
uv pip install -r requirements.txt
```

#### 1.3 Configure Environment Variables
File: `backend/.env`
```env
HUGGINGFACE_ACCESS_TOKEN=your_token_here
GEMINI_API_TOKEN=your_token_here
DATABASE_URL=postgresql://admin:admin123@localhost:5432/product_reviews
```

#### 1.4 Create Database Models
File: `backend/app/models.py`
```python
from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    review_text = Column(Text, nullable=False)
    sentiment = Column(String(50))  # positive, negative, neutral
    confidence_score = Column(Float)
    key_points = Column(Text)  # JSON string dari Gemini
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'review_text': self.review_text,
            'sentiment': self.sentiment,
            'confidence_score': self.confidence_score,
            'key_points': self.key_points,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
```

#### 1.5 Create Sentiment Analyzer Service
File: `backend/app/services/sentiment_analyzer.py`
- Load model: `distilbert-base-uncased-finetuned-sst-2-english`
- Return: `{sentiment: str, confidence: float}`

#### 1.6 Create Gemini Extractor Service
File: `backend/app/services/gemini_extractor.py`
- Extract key points dalam bahasa yang sama dengan input
- Prompt: "Extract key points from this review in the same language as the input. Return as JSON array."

#### 1.7 Create API Endpoints
File: `backend/app/views.py`

**POST /api/analyze-review**
- Input: `{review_text: string}`
- Process:
  1. Analyze sentiment (Hugging Face)
  2. Extract key points (Gemini)
  3. Save to database
- Output: `{id, review_text, sentiment, confidence_score, key_points, created_at}`

**GET /api/reviews**
- Query params: `?page=1&limit=10`
- Output: `{reviews: [], total: int}`

#### 1.8 Configure Pyramid App
File: `backend/app/__init__.py`
- Setup CORS
- Configure routes
- Database connection

File: `backend/development.ini`
- Pyramid configuration
- Server settings

---

### **PHASE 2: Frontend Setup (Vite + React + Bun)**

#### 2.1 Initialize Vite Project
```bash
cd frontend
bun create vite . --template react
bun install
```

#### 2.2 Install Dependencies
```bash
bun add zustand axios
bun add -d prop-types
```

#### 2.3 Setup Shadcn/ui
```bash
bunx shadcn-ui@latest init
# Select: stone theme, CSS variables
```

Install required components:
```bash
bunx shadcn-ui@latest add button
bunx shadcn-ui@latest add card
bunx shadcn-ui@latest add textarea
bunx shadcn-ui@latest add badge
bunx shadcn-ui@latest add skeleton
bunx shadcn-ui@latest add alert
bunx shadcn-ui@latest add dropdown-menu
```

#### 2.4 Create Zustand Store
File: `frontend/src/stores/reviewStore.js`
```javascript
import { create } from 'zustand'

const useReviewStore = create((set) => ({
  reviews: [],
  currentAnalysis: null,
  isLoading: false,
  error: null,
  
  setReviews: (reviews) => set({ reviews }),
  setCurrentAnalysis: (analysis) => set({ currentAnalysis: analysis }),
  setLoading: (loading) => set({ isLoading: loading }),
  setError: (error) => set({ error }),
}))

export default useReviewStore
```

#### 2.5 Create API Client
File: `frontend/src/lib/api.js`
```javascript
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:6543/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

export const analyzeReview = async (reviewText) => {
  const response = await api.post('/analyze-review', { review_text: reviewText })
  return response.data
}

export const getReviews = async (page = 1, limit = 10) => {
  const response = await api.get('/reviews', { params: { page, limit } })
  return response.data
}

export default api
```

#### 2.6 Create Components

**File: `frontend/src/components/ThemeToggle.jsx`**
- Dark/Light mode toggle using shadcn

**File: `frontend/src/components/ReviewForm.jsx`**
- Textarea for review input
- Submit button with loading state
- Error handling display

**File: `frontend/src/components/ReviewResults.jsx`**
- Display sentiment with color-coded badge:
  - Positive: Green
  - Negative: Red
  - Neutral: Yellow
- Display confidence score (progress bar)
- Display key points (bullet list)

**File: `frontend/src/components/ReviewHistory.jsx`**
- Table/List of previous reviews
- Pagination
- Click to view details

#### 2.7 Create Main App
File: `frontend/src/App.jsx`
- Layout with header (title + theme toggle)
- ReviewForm
- ReviewResults (conditional render)
- ReviewHistory

---

### **PHASE 3: Database Setup**

#### 3.1 Create Database Tables
```sql
-- Run this in PostgreSQL or let SQLAlchemy create it
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    review_text TEXT NOT NULL,
    sentiment VARCHAR(50),
    confidence_score FLOAT,
    key_points TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 3.2 Initialize Database in Backend
File: `backend/app/database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv('DATABASE_URL'))
SessionLocal = sessionmaker(bind=engine)

def init_db():
    from .models import Base
    Base.metadata.create_all(bind=engine)
```

---

### **PHASE 4: Integration & Testing**

#### 4.1 Backend Testing
```bash
cd backend
# Activate venv
pserve development.ini
```

Test endpoints:
```bash
# Test analyze endpoint
curl -X POST http://localhost:6543/api/analyze-review \
  -H "Content-Type: application/json" \
  -d '{"review_text": "This product is amazing!"}'

# Test get reviews
curl http://localhost:6543/api/reviews?page=1&limit=10
```

#### 4.2 Frontend Testing
```bash
cd frontend
bun run dev
```

Test:
1. Submit a review
2. Check sentiment analysis appears
3. Check key points display
4. Check history updates
5. Test dark/light mode toggle
6. Test pagination

#### 4.3 Integration Testing
- Submit reviews in different languages (English, Indonesian)
- Verify Gemini extracts key points in same language
- Check database persistence
- Test error scenarios (empty input, API failures)

---

### **PHASE 5: Error Handling & Loading States**

#### 5.1 Backend Error Handling
- Try-catch for API calls (Hugging Face, Gemini)
- Database connection errors
- Validation errors
- Return proper HTTP status codes (400, 500)

#### 5.2 Frontend Error Handling
- Loading spinner during analysis
- Error alerts for failed requests
- Form validation (empty input)
- Network error handling

---

### **PHASE 6: Documentation**

#### 6.1 Main README.md
```markdown
# Product Review Analyzer

## Features
- AI-powered sentiment analysis
- Intelligent key points extraction
- Multi-language support
- Review history with pagination
- Dark/Light theme support

## Tech Stack
### Backend
- Python 3.13
- Pyramid Framework
- SQLAlchemy ORM
- PostgreSQL Database
- Hugging Face Transformers
- Google Gemini AI

### Frontend
- Vite + React
- Shadcn/ui (Stone theme)
- Zustand State Management
- Bun Package Manager

## Setup Instructions
[Include detailed setup steps]

## API Documentation
[Include endpoint details]

## Screenshots
[Include screenshots]
```

#### 6.2 Backend README.md
- Setup instructions
- Environment variables
- Database configuration
- API endpoints documentation

#### 6.3 Frontend README.md
- Setup instructions
- Available scripts
- Component structure
- State management

---

## 🎯 Deliverables Checklist

- [ ] **Backend API with 2 endpoints:**
  - [ ] POST /api/analyze-review (working)
  - [ ] GET /api/reviews (working with pagination)

- [ ] **React Frontend:**
  - [ ] Review input form
  - [ ] Results display (sentiment + key points)
  - [ ] Review history with pagination
  - [ ] Dark/Light theme toggle
  - [ ] Loading states
  - [ ] Error handling

- [ ] **Database Integration:**
  - [ ] SQLAlchemy models
  - [ ] PostgreSQL connection
  - [ ] CRUD operations

- [ ] **AI Integration:**
  - [ ] Hugging Face sentiment analysis
  - [ ] Gemini key points extraction (multi-language)

- [ ] **Error Handling:**
  - [ ] Backend validation
  - [ ] Frontend error displays
  - [ ] API error responses

- [ ] **Documentation:**
  - [ ] Main README.md
  - [ ] Backend README.md
  - [ ] Frontend README.md
  - [ ] API documentation
  - [ ] Setup instructions

- [ ] **PDF Submission:**
  - [ ] tugas_individu3.pdf
  - [ ] Includes: Nama, NIM, GitHub link

---

## 🚀 Quick Start Commands

### Backend
```bash
cd backend
uv venv
.venv\Scripts\activate  # Windows
uv pip install -r requirements.txt
pserve development.ini
```

### Frontend
```bash
cd frontend
bun install
bun run dev
```

---

## 📊 Expected Timeline

1. **Day 1:** Backend setup + Database + Models (3-4 hours)
2. **Day 2:** API endpoints + AI services integration (4-5 hours)
3. **Day 3:** Frontend setup + Shadcn + Basic components (3-4 hours)
4. **Day 4:** State management + API integration (3-4 hours)
5. **Day 5:** Styling + Polish + Testing (3-4 hours)
6. **Day 6:** Documentation + Final testing (2-3 hours)

**Total:** ~20-25 hours

---

## 🎨 UI/UX Features

### Color Coding
- **Positive Sentiment:** Green badge + success message
- **Negative Sentiment:** Red badge + error styling
- **Neutral Sentiment:** Yellow/Orange badge

### Themes
- **Stone theme** from shadcn/ui
- **Dark mode:** Automatic dark variants
- **Light mode:** Clean, professional look

### Animations
- Smooth transitions for sentiment results
- Loading skeletons during API calls
- Fade-in for history items

---

## 🔒 Security Considerations

1. **Environment Variables:** Never commit .env files
2. **API Keys:** Store securely in .env
3. **Database Credentials:** Use environment variables
4. **CORS:** Configure properly for local development
5. **Input Validation:** Sanitize user inputs

---

## 📝 Notes

- **Multi-language Support:** Gemini will respond in the same language as input
- **Pagination:** Default 10 items per page
- **Sentiment Model:** Using `distilbert-base-uncased-finetuned-sst-2-english`
- **Local Only:** No deployment configuration needed

---

**Good luck with your implementation! 🚀**
