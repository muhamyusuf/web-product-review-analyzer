# Product Review Analyzer - Backend

Backend API untuk Product Review Analyzer menggunakan Python Pyramid framework.

## 🚀 Features

- **Sentiment Analysis** menggunakan Hugging Face Transformers (DistilBERT)
- **Key Points Extraction** menggunakan Google Gemini AI
- **RESTful API** dengan Pyramid framework
- **PostgreSQL Database** dengan SQLAlchemy ORM
- **CORS Support** untuk frontend integration

## 📋 Tech Stack

- Python 3.13
- Pyramid 2.0.2
- SQLAlchemy 2.0.23
- PostgreSQL
- Hugging Face Transformers
- Google Generative AI (Gemini)
- UV (package manager)

## 🛠️ Setup Instructions

### 1. Prerequisites

- Python 3.13
- PostgreSQL (running di `localhost:5432`)
- UV package manager

### 2. Install UV (jika belum ada)

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Setup Virtual Environment

```bash
cd backend
uv venv
.venv\Scripts\activate  # Windows
```

### 4. Install Dependencies

```bash
uv pip install -r requirements.txt
uv pip install -e .
```

### 5. Configure Environment Variables

Buat file `.env` di folder `backend/`:

```env
HUGGINGFACE_ACCESS_TOKEN=your_huggingface_token_here
GEMINI_API_TOKEN=your_gemini_api_token_here
DATABASE_URL=postgresql://admin:admin123@localhost:5432/product_reviews
```

### 6. Initialize Database

Database akan otomatis dibuat saat aplikasi pertama kali dijalankan.
Pastikan PostgreSQL sudah running dan database `product_reviews` sudah ada.

```sql
-- Buat database (jalankan di PostgreSQL)
CREATE DATABASE product_reviews;
```

### 7. Run Server

```bash
pserve development.ini
```

Server akan running di: `http://localhost:6543`

## 📡 API Endpoints

### 1. Health Check

```http
GET /api/health

Response:
{
  "status": "healthy",
  "service": "Product Review Analyzer API"
}
```

### 2. Analyze Review

```http
POST /api/analyze-review
Content-Type: application/json

Request Body:
{
  "review_text": "This product is amazing! Great quality and fast shipping."
}

Response (201):
{
  "status": "success",
  "data": {
    "id": 1,
    "review_text": "This product is amazing! Great quality and fast shipping.",
    "sentiment": "positive",
    "confidence_score": 0.9987,
    "key_points": "[\"Great quality product\", \"Fast shipping service\"]",
    "created_at": "2025-12-06T16:30:00"
  }
}

Error Response (400/500):
{
  "status": "error",
  "error": "Error message here"
}
```

### 3. Get All Reviews

```http
GET /api/reviews?page=1&limit=10

Response:
{
  "status": "success",
  "data": {
    "reviews": [...],
    "total": 25,
    "page": 1,
    "limit": 10,
    "total_pages": 3
  }
}
```

## 📂 Project Structure

```
backend/
├── app/
│   ├── __init__.py          # Pyramid app factory
│   ├── models.py            # SQLAlchemy models
│   ├── views.py             # API endpoints
│   ├── database.py          # Database configuration
│   └── services/
│       ├── sentiment_analyzer.py  # Hugging Face integration
│       └── gemini_extractor.py    # Gemini AI integration
├── development.ini          # Pyramid configuration
├── setup.py                 # Package setup
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables (DO NOT COMMIT)
```

## 🔧 Development

### Running Tests

```bash
# TODO: Add tests
pytest
```

### Database Migration

Gunakan Alembic untuk database migration (optional):

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## 🐛 Troubleshooting

### Error: Database connection failed

- Pastikan PostgreSQL running
- Check DATABASE_URL di `.env`
- Pastikan database `product_reviews` sudah dibuat

### Error: Hugging Face model download failed

- Check internet connection
- Verify HUGGINGFACE_ACCESS_TOKEN
- Model akan otomatis download saat pertama kali dijalankan

### Error: Gemini API failed

- Verify GEMINI_API_TOKEN di `.env`
- Check API quota/limits

## 📝 Notes

- Server default running di port 6543
- CORS enabled untuk semua origins (development only)
- Database tables akan otomatis dibuat saat first run

## 🔒 Security

⚠️ **PENTING:**
- Jangan commit file `.env` ke git
- Gunakan environment variables untuk production
- Update CORS settings untuk production

## 📞 Support

Untuk issues atau pertanyaan, silakan buat issue di repository.
