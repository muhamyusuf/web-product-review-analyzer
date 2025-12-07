# Product Review Analyzer 🚀

Aplikasi web untuk menganalisis product review menggunakan AI. Aplikasi ini menggunakan **Hugging Face Transformers** untuk sentiment analysis dan **Google Gemini AI** untuk ekstraksi key points dari review.

## 📸 Screenshots

Display all apps
![Screenshot](./assets/screenshot-website.png)

After submit the form
![Screenshot](./assets/image.png)

## ✨ Features

### 🤖 AI-Powered Analysis
- **Sentiment Analysis**: Menggunakan DistilBERT model dari Hugging Face untuk mendeteksi sentimen (Positive/Negative/Neutral)
- **Key Points Extraction**: Menggunakan Google Gemini AI untuk mengekstrak poin-poin penting dari review
- **Multi-language Support**: Mendukung review dalam berbagai bahasa (Gemini akan respond dalam bahasa yang sama)

### 💻 User Interface
- **Modern Design**: UI yang clean dan professional menggunakan Shadcn/ui dengan Stone theme
- **Dark/Light Mode**: Toggle theme dengan persistence ke localStorage
- **Real-time Analysis**: Loading states dan error handling yang smooth
- **Review History**: Pagination untuk melihat riwayat review
- **Responsive**: Bekerja di semua ukuran layar

### 🔧 Technical Features
- **RESTful API**: Backend dengan Pyramid framework
- **PostgreSQL Database**: Persistent storage dengan SQLAlchemy ORM
- **State Management**: Zustand untuk efficient state management
- **Type Safety**: PropTypes untuk React components

## 🏗️ Tech Stack

### Backend
- **Framework**: Python Pyramid 2.0.2
- **Database**: PostgreSQL + SQLAlchemy 2.0.23
- **AI/ML**:
  - Hugging Face Transformers (DistilBERT)
  - Google Generative AI (Gemini Pro)
- **Package Manager**: UV
- **Server**: Waitress

### Frontend
- **Framework**: React 18 + Vite 5
- **UI Library**: Shadcn/ui (Stone theme)
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **HTTP Client**: Axios
- **Icons**: Lucide React
- **Package Manager**: Bun

## 📋 Prerequisites

Sebelum memulai, pastikan sudah install:

- **Python 3.13**
- **PostgreSQL** (running di localhost:5432)
- **Node.js 18+** atau **Bun**
- **UV** (Python package manager)

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone <repository-url>
cd web-product-review-analyzer
```

### 2. Setup Database

Buat database PostgreSQL:

```sql
CREATE DATABASE product_reviews;
```

### 3. Setup Backend

```bash
cd backend

# Create virtual environment
uv venv
.venv\Scripts\activate  # Windows

# Install dependencies
uv pip install -r requirements.txt
uv pip install -e .

# Configure environment variables
# Edit file .env dengan:
# HUGGINGFACE_ACCESS_TOKEN=your_token
# GEMINI_API_TOKEN=your_token
# DATABASE_URL=postgresql://admin:admin123@localhost:5432/product_reviews

# Run server
pserve development.ini
```

Backend akan running di: `http://localhost:6543`

### 4. Setup Frontend

```bash
cd frontend

# Install dependencies
bun install

# Run dev server
bun run dev
```

Frontend akan running di: `http://localhost:5173`

## 📡 API Documentation

### POST /api/analyze-review

Analyze product review dan simpan ke database.

**Request:**
```json
{
  "review_text": "This product is amazing! Great quality and fast shipping."
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "review_text": "This product is amazing!...",
    "sentiment": "positive",
    "confidence_score": 0.9987,
    "key_points": "[\"Great quality\", \"Fast shipping\"]",
    "created_at": "2025-12-06T16:30:00"
  }
}
```

### GET /api/reviews?page=1&limit=10

Get semua reviews dengan pagination.

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

## 📂 Project Structure

```
web-product-review-analyzer/
├── backend/
│   ├── app/
│   │   ├── models.py              # SQLAlchemy models
│   │   ├── views.py               # API endpoints
│   │   ├── database.py            # DB configuration
│   │   └── services/
│   │       ├── sentiment_analyzer.py
│   │       └── gemini_extractor.py
│   ├── development.ini
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/                # Shadcn components
│   │   │   ├── ReviewForm.jsx
│   │   │   ├── ReviewResults.jsx
│   │   │   ├── ReviewHistory.jsx
│   │   │   └── ThemeToggle.jsx
│   │   ├── stores/
│   │   │   └── reviewStore.js
│   │   ├── lib/
│   │   │   └── api.js
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

## 🎯 Deliverables Checklist

- ✅ **Backend API**
  - ✅ POST /api/analyze-review
  - ✅ GET /api/reviews (with pagination)
  - ✅ Hugging Face integration
  - ✅ Gemini AI integration

- ✅ **Frontend**
  - ✅ Review input form
  - ✅ Results display
  - ✅ Review history
  - ✅ Dark/Light mode
  - ✅ Error handling
  - ✅ Loading states

- ✅ **Database**
  - ✅ SQLAlchemy models
  - ✅ PostgreSQL integration
  - ✅ CRUD operations

- ✅ **Documentation**
  - ✅ Main README
  - ✅ Backend README
  - ✅ Frontend README
  - ✅ API documentation

## 🎨 UI/UX Highlights

### Color-Coded Sentiments
- **🟢 Positive**: Green badge dengan confidence score
- **🔴 Negative**: Red badge dengan confidence score
- **🟡 Neutral**: Yellow badge dengan confidence score

### Smooth Animations
- Fade-in untuk results display
- Loading spinner saat analysis
- Smooth theme transitions

### Professional Design
- Clean layout dengan Shadcn/ui
- Consistent spacing dan typography
- Accessible color contrasts

## 🔧 Development

### Backend Development

```bash
cd backend
.venv\Scripts\activate
pserve development.ini --reload
```

### Frontend Development

```bash
cd frontend
bun run dev
```

### Database Management

**View tables:**
```sql
\dt  -- PostgreSQL
```

**View reviews:**
```sql
SELECT * FROM reviews ORDER BY created_at DESC;
```

## 🐛 Troubleshooting

### Backend Issues

**Database connection error:**
- Check PostgreSQL is running
- Verify DATABASE_URL in `.env`
- Ensure database exists

**AI model errors:**
- Verify API tokens in `.env`
- Check internet connection (first-time model download)
- Check API quotas

### Frontend Issues

**Cannot connect to API:**
- Ensure backend is running on port 6543
- Check CORS settings
- Verify API_BASE_URL in `lib/api.js`

**Theme not persisting:**
- Clear browser localStorage
- Check browser console for errors

## 📝 Environment Variables

### Backend (.env)

```env
HUGGINGFACE_ACCESS_TOKEN=your_huggingface_token
GEMINI_API_TOKEN=your_gemini_token
DATABASE_URL=postgresql://admin:admin123@localhost:5432/product_reviews
```

### Frontend

Frontend tidak memerlukan `.env` untuk development lokal.

## 🔒 Security Notes

⚠️ **IMPORTANT:**
- Jangan commit file `.env` ke repository
- Gunakan `.gitignore` untuk exclude sensitive files
- Update CORS policy untuk production
- Use HTTPS in production

## 📦 Deployment

> **Note**: Aplikasi ini didesain untuk lokal development. Untuk production deployment, pertimbangkan:

- Environment-specific configuration
- Production database setup
- HTTPS/SSL certificates
- API rate limiting
- Error monitoring (Sentry, etc.)

## 🎓 Assignment Information

**Mata Kuliah**: [Nama Mata Kuliah]  
**Tugas**: Individu 3 - Product Review Analyzer  
**Teknologi**:
- Backend: Python Pyramid + SQLAlchemy + PostgreSQL
- Frontend: Vite + React + Shadcn/ui + Zustand
- AI: Hugging Face + Google Gemini

## 👨‍💻 Kontributor

- **Nama**: [Your Name]
- **NIM**: [Your NIM]

## 📄 License

MIT License - feel free to use for educational purposes.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) untuk sentiment analysis models
- [Google Gemini AI](https://ai.google.dev/) untuk key points extraction
- [Shadcn/ui](https://ui.shadcn.com/) untuk beautiful UI components
- [Pyramid](https://trypyramid.com/) framework

---

**Happy Coding! 🚀**

Jika ada pertanyaan atau issues, silakan buat issue di repository ini.
