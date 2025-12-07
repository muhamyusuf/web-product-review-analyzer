# 📁 Project Structure - Product Review Analyzer

Complete file tree dan penjelasan setiap file/folder.

## 🌳 Directory Tree

```
web-product-review-analyzer/
│
├── 📄 README.md                          # Main documentation
├── 📄 IMPLEMENTATION_PLAN.md             # Detailed implementation plan
├── 📄 QUICK_START.md                     # Quick start guide
├── 📄 SUBMISSION_TEMPLATE.md             # PDF submission template
├── 📄 .gitignore                         # Git ignore rules
├── 📄 product-review-analyzer.code-workspace  # VS Code workspace
│
├── 📁 backend/                           # Python Pyramid Backend
│   ├── 📄 .env                           # Environment variables (DO NOT COMMIT!)
│   ├── 📄 .env.example                   # Environment template
│   ├── 📄 .gitignore                     # Backend git ignore
│   ├── 📄 README.md                      # Backend documentation
│   ├── 📄 requirements.txt               # Python dependencies
│   ├── 📄 setup.py                       # Package setup
│   ├── 📄 development.ini                # Pyramid configuration
│   ├── 📄 MANIFEST.in                    # Package manifest
│   ├── 📄 test_api.py                    # API test script
│   │
│   └── 📁 app/                           # Main application package
│       ├── 📄 __init__.py                # Pyramid app factory + CORS
│       ├── 📄 models.py                  # SQLAlchemy models (Review)
│       ├── 📄 views.py                   # API endpoints
│       ├── 📄 database.py                # Database configuration
│       │
│       └── 📁 services/                  # AI Services
│           ├── 📄 __init__.py
│           ├── 📄 sentiment_analyzer.py  # Hugging Face integration
│           └── 📄 gemini_extractor.py    # Gemini AI integration
│
└── 📁 frontend/                          # React + Vite Frontend
    ├── 📄 .gitignore                     # Frontend git ignore
    ├── 📄 README.md                      # Frontend documentation
    ├── 📄 package.json                   # Node dependencies
    ├── 📄 vite.config.js                 # Vite configuration
    ├── 📄 tailwind.config.js             # Tailwind CSS config
    ├── 📄 postcss.config.js              # PostCSS config
    ├── 📄 components.json                # Shadcn/ui config
    ├── 📄 jsconfig.json                  # VS Code path aliases
    ├── 📄 .eslintrc.cjs                  # ESLint configuration
    ├── 📄 index.html                     # HTML entry point
    │
    └── 📁 src/                           # Source files
        ├── 📄 main.jsx                   # React entry point
        ├── 📄 App.jsx                    # Main App component
        ├── 📄 index.css                  # Global styles + Tailwind
        │
        ├── 📁 components/                # React components
        │   ├── 📄 ThemeToggle.jsx        # Dark/Light mode toggle
        │   ├── 📄 ReviewForm.jsx         # Review input form
        │   ├── 📄 ReviewResults.jsx      # Analysis results display
        │   ├── 📄 ReviewHistory.jsx      # Reviews history list
        │   │
        │   └── 📁 ui/                    # Shadcn/ui components
        │       ├── 📄 card.jsx
        │       ├── 📄 button.jsx
        │       ├── 📄 textarea.jsx
        │       ├── 📄 badge.jsx
        │       └── 📄 alert.jsx
        │
        ├── 📁 stores/                    # State management
        │   └── 📄 reviewStore.js         # Zustand store
        │
        └── 📁 lib/                       # Utilities
            ├── 📄 api.js                 # Axios API client
            └── 📄 utils.js               # Helper functions
```

---

## 📝 File Descriptions

### Root Level Files

| File | Purpose |
|------|---------|
| `README.md` | Main project documentation, setup guide, features overview |
| `IMPLEMENTATION_PLAN.md` | Detailed step-by-step implementation plan with phases |
| `QUICK_START.md` | Quick start guide untuk running aplikasi ASAP |
| `SUBMISSION_TEMPLATE.md` | Template untuk PDF submission (nama, NIM, screenshots) |
| `.gitignore` | Files/folders yang tidak di-track oleh Git |
| `product-review-analyzer.code-workspace` | VS Code workspace settings |

---

### Backend Files

#### Configuration Files

| File | Purpose | Important Notes |
|------|---------|-----------------|
| `.env` | Environment variables (API keys, DB URL) | ⚠️ **NEVER COMMIT!** |
| `.env.example` | Template untuk `.env` | Safe to commit |
| `requirements.txt` | Python package dependencies | Run: `uv pip install -r requirements.txt` |
| `setup.py` | Package setup untuk Pyramid | Required for `pserve` |
| `development.ini` | Pyramid server configuration | Port 6543 |
| `MANIFEST.in` | Package manifest for distribution | - |

#### Application Files

| File | Purpose | Key Components |
|------|---------|----------------|
| `app/__init__.py` | Pyramid app factory | CORS setup, routes, config |
| `app/models.py` | Database models | `Review` model with SQLAlchemy |
| `app/views.py` | API endpoints | `/analyze-review`, `/reviews` |
| `app/database.py` | Database connection | SessionFactory, init_db() |
| `app/services/sentiment_analyzer.py` | Sentiment analysis | Hugging Face DistilBERT |
| `app/services/gemini_extractor.py` | Key points extraction | Google Gemini AI |

#### Testing

| File | Purpose |
|------|---------|
| `test_api.py` | API testing script | Test all endpoints |

---

### Frontend Files

#### Configuration Files

| File | Purpose | Usage |
|------|---------|-------|
| `package.json` | Node.js dependencies & scripts | `bun install` |
| `vite.config.js` | Vite bundler config | Dev server port 5173 |
| `tailwind.config.js` | Tailwind CSS theme | Stone theme, dark mode |
| `postcss.config.js` | PostCSS plugins | Tailwind + Autoprefixer |
| `components.json` | Shadcn/ui configuration | Component aliases |
| `jsconfig.json` | VS Code IntelliSense | Path aliases (`@/*`) |
| `.eslintrc.cjs` | ESLint rules | React best practices |

#### Application Files

| File | Purpose | Components |
|------|---------|-------------|
| `index.html` | HTML entry point | Root div, Google Fonts |
| `src/main.jsx` | React app mount | ReactDOM.render |
| `src/App.jsx` | Main application | Layout, routing, state |
| `src/index.css` | Global styles | Tailwind, theme variables |

#### React Components

| Component | Purpose | Features |
|-----------|---------|----------|
| `ThemeToggle.jsx` | Theme switcher | localStorage persistence |
| `ReviewForm.jsx` | Review input | Validation, loading states |
| `ReviewResults.jsx` | Show analysis | Sentiment badges, key points |
| `ReviewHistory.jsx` | Reviews list | Pagination, timestamps |

#### UI Components (Shadcn)

| Component | Usage |
|-----------|-------|
| `ui/card.jsx` | Content containers |
| `ui/button.jsx` | Interactive buttons |
| `ui/textarea.jsx` | Multi-line input |
| `ui/badge.jsx` | Sentiment indicators |
| `ui/alert.jsx` | Error messages |

#### State & API

| File | Purpose | Key Functions |
|------|---------|---------------|
| `stores/reviewStore.js` | Global state (Zustand) | reviews, isLoading, error |
| `lib/api.js` | API client (Axios) | analyzeReview(), getReviews() |
| `lib/utils.js` | Helper functions | cn() for className merging |

---

## 🔐 Sensitive Files (Never Commit!)

```
⚠️ NEVER COMMIT THESE FILES:
├── backend/.env                  # Contains API keys!
├── backend/.venv/                # Virtual environment
├── backend/__pycache__/          # Python cache
├── frontend/node_modules/        # npm packages
└── frontend/dist/                # Build output
```

All protected by `.gitignore` files ✅

---

## 📦 Generated Files/Folders (Auto-created)

### Backend
- `.venv/` - Virtual environment (created by `uv venv`)
- `__pycache__/` - Python bytecode cache
- `*.egg-info/` - Package metadata

### Frontend
- `node_modules/` - npm packages (created by `bun install`)
- `dist/` - Production build (created by `bun run build`)

---

## 🎯 Important File Relationships

### Backend Flow
```
development.ini
    ↓
app/__init__.py (Pyramid app)
    ↓
app/views.py (API endpoints)
    ↓
├── app/services/sentiment_analyzer.py (Hugging Face)
└── app/services/gemini_extractor.py (Gemini)
    ↓
app/models.py (Database)
    ↓
PostgreSQL Database
```

### Frontend Flow
```
index.html
    ↓
src/main.jsx
    ↓
src/App.jsx
    ↓
├── components/ReviewForm.jsx
├── components/ReviewResults.jsx
└── components/ReviewHistory.jsx
    ↓
stores/reviewStore.js (Zustand)
    ↓
lib/api.js (Axios)
    ↓
Backend API (http://localhost:6543)
```

---

## 📊 File Count Summary

| Category | Count |
|----------|-------|
| **Total Files** | ~50 files |
| **Backend Python** | 9 files |
| **Frontend React** | 15 files |
| **Config Files** | 12 files |
| **Documentation** | 5 files |
| **UI Components** | 5 files |

---

## 🎨 Code Organization Principles

### Backend (Python)
- ✅ **Separation of Concerns**: Models, Views, Services
- ✅ **Service Layer**: AI operations isolated
- ✅ **ORM Pattern**: SQLAlchemy for database
- ✅ **Configuration**: INI file + environment variables

### Frontend (React)
- ✅ **Component-Based**: Reusable UI components
- ✅ **State Management**: Centralized with Zustand
- ✅ **API Layer**: Separated from components
- ✅ **Styling**: Utility-first with Tailwind CSS

---

## 🔍 Where to Find What?

**Need to change...**

| What | Where |
|------|-------|
| API endpoints | `backend/app/views.py` |
| Database schema | `backend/app/models.py` |
| AI prompts | `backend/app/services/gemini_extractor.py` |
| Sentiment model | `backend/app/services/sentiment_analyzer.py` |
| UI components | `frontend/src/components/` |
| Color theme | `frontend/src/index.css` |
| API base URL | `frontend/src/lib/api.js` |
| State logic | `frontend/src/stores/reviewStore.js` |
| Server port | `backend/development.ini` |

---

**Project structure optimized for maintainability and scalability! 🚀**
