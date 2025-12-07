# 🚀 Quick Start Guide - Product Review Analyzer

Panduan lengkap untuk menjalankan aplikasi dari awal.

---

## 📋 Prerequisites Checklist

Sebelum mulai, pastikan sudah install:

- [ ] Python 3.13
- [ ] PostgreSQL (running)
- [ ] Bun atau Node.js 18+
- [ ] UV (Python package manager)
- [ ] Git

---

## 🔧 Step-by-Step Setup

### STEP 1: Clone & Prepare

```bash
# Clone repository (atau download ZIP)
git clone <repository-url>
cd web-product-review-analyzer

# Buka folder di VS Code atau editor favorit
code .
```

---

### STEP 2: Setup PostgreSQL Database

1. **Buka PostgreSQL (pgAdmin atau terminal)**

2. **Buat database baru:**
```sql
CREATE DATABASE product_reviews;
```

3. **Verify connection:**
```sql
-- Test connection
\c product_reviews  -- PostgreSQL
```

Default credentials di tutorial ini:
- Username: `admin`
- Password: `admin123`
- Host: `localhost`
- Port: `5432`

**📝 Note**: Jika credentials berbeda, update di `.env` nanti!

---

### STEP 3: Get API Keys

#### A. Hugging Face Token

1. Buka: https://huggingface.co/
2. Sign up/Login
3. Go to: Settings → Access Tokens
4. Create New Token (read permission)
5. Copy token (contoh: `hf_xxxxxxxxxxxxx`)

#### B. Google Gemini API Token

1. Buka: https://makersuite.google.com/app/apikey
2. Login dengan Google Account
3. Create API Key
4. Copy API Key (contoh: `AIzaSyxxxxxxxxxxxxx`)

**⚠️ PENTING**: Simpan kedua token ini, akan digunakan di Step 4!

---

### STEP 4: Setup Backend

```bash
# Masuk ke folder backend
cd backend

# Install UV jika belum ada (Windows PowerShell)
# powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create virtual environment dengan UV
uv venv

# Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac/Linux

# Install dependencies
uv pip install -r requirements.txt

# Install package dalam editable mode
uv pip install -e .
```

**Configure Environment Variables:**

1. Copy template `.env.example` ke `.env`:
```bash
copy .env.example .env  # Windows
# cp .env.example .env   # Mac/Linux
```

2. Edit file `.env` dengan text editor:
```env
# File: backend/.env
HUGGINGFACE_ACCESS_TOKEN=hf_xxxxxxxxxxxxx  # Paste token dari Step 3A
GEMINI_API_TOKEN=AIzaSyxxxxxxxxxxxxx       # Paste token dari Step 3B
DATABASE_URL=postgresql://admin:admin123@localhost:5432/product_reviews
```

3. Save file `.env`

**⚠️ WARNING**: Jangan commit file `.env` ke git!

---

### STEP 5: Run Backend Server

```bash
# Masih di folder backend dengan venv active
pserve development.ini

# Expected output:
# Starting server in PID 12345
# Serving on http://localhost:6543
```

**✅ Test Backend:**

Buka browser: http://localhost:6543/api/health

Expected response:
```json
{
  "status": "healthy",
  "service": "Product Review Analyzer API"
}
```

Jika berhasil, **JANGAN TUTUP TERMINAL INI!** Backend harus tetap running.

---

### STEP 6: Setup Frontend (Terminal Baru)

Buka **terminal baru** (Ctrl + Shift + ` di VS Code)

```bash
# Masuk ke folder frontend
cd frontend

# Install Bun jika belum ada (Windows PowerShell)
# powershell -c "irm bun.sh/install.ps1 | iex"

# Install dependencies dengan Bun
bun install

# Alternative: Gunakan npm jika tidak ada Bun
# npm install
```

---

### STEP 7: Run Frontend Dev Server

```bash
# Masih di folder frontend
bun run dev

# Alternative dengan npm:
# npm run dev

# Expected output:
# VITE v5.0.8  ready in 500 ms
# ➜  Local:   http://localhost:5173/
# ➜  Network: use --host to expose
```

---

### STEP 8: Access Application

1. **Buka browser**: http://localhost:5173

2. **Verify:**
   - ✅ Page loading dengan "Product Review Analyzer" header
   - ✅ Ada form untuk input review
   - ✅ Theme toggle (moon/sun icon) di header

---

## 🎯 Testing Application

### Test 1: English Review (Positive)

1. Di form review, paste teks ini:
```
This product is absolutely amazing! The quality is outstanding and the shipping was incredibly fast. Highly recommend to everyone!
```

2. Click **"Analyze Review"**

3. **Expected Results:**
   - Sentiment: 🟢 **Positive** (confidence ~95%+)
   - Key Points (English):
     - Outstanding quality
     - Fast shipping
     - Highly recommended

### Test 2: Indonesian Review (Negative)

1. Clear form, paste teks ini:
```
Produk ini sangat mengecewakan. Kualitasnya buruk dan tidak sesuai deskripsi. Pengiriman juga sangat lambat. Tidak rekomen!
```

2. Click **"Analyze Review"**

3. **Expected Results:**
   - Sentiment: 🔴 **Negative** (confidence ~90%+)
   - Key Points (Bahasa Indonesia):
     - Kualitas buruk
     - Tidak sesuai deskripsi
     - Pengiriman lambat

### Test 3: Review History

1. Scroll down
2. Lihat section "Review History"
3. Verify:
   - ✅ Kedua review muncul di history
   - ✅ Ada pagination controls jika > 10 reviews

### Test 4: Dark Mode

1. Click icon moon/sun di header
2. Verify:
   - ✅ Theme berubah smooth
   - ✅ Persistent (reload page, theme tetap)

---

## 🐛 Troubleshooting

### Problem: Backend tidak start

**Error: "Database connection failed"**
```bash
# Solution:
# 1. Check PostgreSQL is running
# 2. Verify database exists:
psql -U admin -d product_reviews

# 3. Check .env DATABASE_URL
```

**Error: "No module named 'app'"**
```bash
# Solution: Install package in editable mode
cd backend
.venv\Scripts\activate
uv pip install -e .
```

**Error: "ModuleNotFoundError: transformers"**
```bash
# Solution: Reinstall dependencies
uv pip install -r requirements.txt
```

---

### Problem: Frontend tidak start

**Error: "Cannot find module '@/...'"**
```bash
# Solution: Reinstall dependencies
cd frontend
rm -rf node_modules
bun install
```

**Error: "Failed to fetch from API"**
- Check backend is running di port 6543
- Test: http://localhost:6543/api/health

---

### Problem: AI Analysis Failed

**Error: "Sentiment analysis failed"**
- Verify HUGGINGFACE_ACCESS_TOKEN di `.env`
- Wait for model download (first time ~500MB)
- Check internet connection

**Error: "Key points extraction failed"**
- Verify GEMINI_API_TOKEN di `.env`
- Check Gemini API quota
- Verify internet connection

---

## 📦 Stopping the Application

1. **Stop Frontend**:
   - Go to frontend terminal
   - Press `Ctrl + C`

2. **Stop Backend**:
   - Go to backend terminal
   - Press `Ctrl + C`

3. **Deactivate venv**:
   ```bash
   deactivate
   ```

---

## 🔄 Restarting the Application

Lain kali mau jalankan lagi:

```bash
# Terminal 1: Backend
cd backend
.venv\Scripts\activate
pserve development.ini

# Terminal 2: Frontend (terminal baru)
cd frontend
bun run dev
```

Access: http://localhost:5173

---

## 📸 Taking Screenshots for PDF

Untuk submission PDF, ambil screenshots:

1. **Homepage** - Form review kosong
2. **Positive Analysis** - Review dengan sentiment positive
3. **Negative Analysis** - Review dengan sentiment negative
4. **Review History** - List semua reviews
5. **Dark Mode** - Toggle dark mode
6. **Mobile View** - Responsive di mobile (gunakan Chrome DevTools)

---

## 🎓 Creating Submission PDF

1. **Update SUBMISSION_TEMPLATE.md** dengan:
   - Nama & NIM
   - Link GitHub repository
   - Screenshots

2. **Convert to PDF**:
   - Method 1: Print to PDF dari browser
   - Method 2: Use Markdown to PDF converter
   - Method 3: Copy ke Word, lalu Save as PDF

3. **Filename**: `tugas_individu3.pdf`

---

## ✅ Final Checklist

Sebelum submit, pastikan:

- [ ] Backend running tanpa error
- [ ] Frontend running tanpa error
- [ ] Database ada data reviews
- [ ] Semua fitur bekerja:
  - [ ] Input review
  - [ ] Sentiment analysis
  - [ ] Key points extraction
  - [ ] Review history
  - [ ] Pagination
  - [ ] Dark/Light mode
- [ ] Screenshots diambil
- [ ] Repository di-push ke GitHub
- [ ] README.md updated
- [ ] PDF submission ready

---

## 🎉 Selesai!

Jika semua langkah di atas berhasil, aplikasi Product Review Analyzer sudah siap digunakan!

**Need Help?**
- Baca README.md di root folder
- Check backend/README.md untuk backend details
- Check frontend/README.md untuk frontend details
- Review IMPLEMENTATION_PLAN.md untuk architecture

**Happy Coding! 🚀**
