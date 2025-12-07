# Tugas Individu 3 - Product Review Analyzer

## Informasi Mahasiswa

**Nama**: Muhammad Yusuf  
**NIM**: 122140193  
**Mata Kuliah**: Pengembangan Aplikasi Web RA  
**Dosen**: Muhammad Habib Algifari, S.Kom., M.TI.

---

## Link Repository GitHub

🔗 **GitHub Repository**: [https://github.com/muhamyusuf/web-product-review-analyzer](https://github.com/muhamyusuf/web-product-review-analyzer)

---

## Deskripsi Aplikasi

Product Review Analyzer adalah aplikasi web berbasis AI yang dapat menganalisis sentiment dari product review dan mengekstrak key points penting menggunakan:

- **Sentiment Analysis**: Hugging Face Transformers (DistilBERT model)
- **Key Points Extraction**: Google Gemini AI
- **Full-stack Application**: Backend API dengan Pyramid + Frontend React

### Fitur Utama:

1. ✅ Input product review (support multi-language)
2. ✅ AI sentiment analysis (Positive/Negative/Neutral)
3. ✅ Confidence score visualization
4. ✅ Key points extraction dalam bahasa yang sama dengan input
5. ✅ Review history dengan pagination
6. ✅ Dark/Light mode theme
7. ✅ PostgreSQL database integration
8. ✅ Error handling dan loading states

---

## Tech Stack

### Backend
- Python 3.13
- Pyramid Framework 2.0.2
- SQLAlchemy 2.0.23 (ORM)
- PostgreSQL Database
- UV (Package Manager)
- Hugging Face Transformers
- Google Generative AI (Gemini)

### Frontend
- React 18
- Vite 5
- Shadcn/ui (Stone Theme)
- Zustand (State Management)
- Tailwind CSS
- Bun (Package Manager)

---

## API Endpoints

### 1. POST /api/analyze-review
Menganalisis review baru dan menyimpan ke database.

**Request Body:**
```json
{
  "review_text": "This product is amazing!"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "review_text": "This product is amazing!",
    "sentiment": "positive",
    "confidence_score": 0.9987,
    "key_points": "[\"Great quality\"]",
    "created_at": "2025-12-06T16:30:00"
  }
}
```

### 2. GET /api/reviews?page=1&limit=10
Mendapatkan semua reviews dengan pagination.

**Response:**
```json
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

---

## Database Schema

### Table: reviews

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary Key (Auto Increment) |
| review_text | TEXT | Teks review dari user |
| sentiment | VARCHAR(50) | Sentiment: positive/negative/neutral |
| confidence_score | FLOAT | Confidence score (0-1) |
| key_points | TEXT | JSON array dari key points |
| created_at | TIMESTAMP | Waktu pembuatan |

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone <repository-url>
cd web-product-review-analyzer
```

### 2. Setup Backend
```bash
cd backend
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
uv pip install -e .

# Configure .env dengan API tokens
# HUGGINGFACE_ACCESS_TOKEN=...
# GEMINI_API_TOKEN=...

pserve development.ini
```

### 3. Setup Frontend
```bash
cd frontend
bun install
bun run dev
```

### 4. Access Application
- Backend API: http://localhost:6543
- Frontend: http://localhost:5173

---

## Screenshots

> **Note**: Tambahkan screenshots aplikasi di sini:
> 1. Landing page / Review form
> 2. Analysis results (positive sentiment)
> 3. Analysis results (negative sentiment)
> 4. Review history
> 5. Dark mode

[Paste screenshots here]

---

## Deliverables Checklist

- ✅ Working backend API dengan 2 endpoints
  - ✅ POST /api/analyze-review
  - ✅ GET /api/reviews
- ✅ React frontend dengan:
  - ✅ Form input review
  - ✅ Results display (sentiment + key points)
  - ✅ Review history dengan pagination
- ✅ Database integration (SQLAlchemy + PostgreSQL)
- ✅ Error handling dan loading states
- ✅ Documentation (README.md)
- ✅ Dark/Light mode theme

---

## Tantangan & Solusi

### Tantangan 1: Model Download Time
**Problem**: Hugging Face model download memakan waktu lama saat pertama kali.
**Solution**: Menggunakan `distilbert` yang lebih ringan dan caching model.

### Tantangan 2: Multi-language Support
**Problem**: Key points harus dalam bahasa yang sama dengan input.
**Solution**: Menggunakan Gemini AI dengan prompt engineering yang spesifik.

### Tantangan 3: State Management
**Problem**: Sinkronisasi state antara form, results, dan history.
**Solution**: Menggunakan Zustand untuk centralized state management.

---

## Kesimpulan

Aplikasi Product Review Analyzer berhasil dibuat dengan fitur-fitur:
- AI-powered sentiment analysis menggunakan Hugging Face
- Key points extraction menggunakan Google Gemini
- Full-stack application dengan Python Pyramid dan React
- Database integration untuk persistent storage
- Modern UI dengan dark/light mode

Aplikasi ini menunjukkan integrasi antara multiple AI services, modern web frameworks, dan best practices dalam development.

---

**Tanggal Pengumpulan**: [07/12/2025]

**Contribute by**:

Muhammad Yusuf
