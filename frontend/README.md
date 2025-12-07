# Product Review Analyzer - Frontend

Frontend aplikasi Product Review Analyzer menggunakan React + Vite + Shadcn/ui.

## 🚀 Features

- **Modern UI** dengan Shadcn/ui components
- **Dark/Light Mode** dengan theme toggle
- **Real-time Analysis** dengan loading states
- **Review History** dengan pagination
- **Responsive Design** untuk semua device sizes
- **Multi-language Support** untuk review input

## 📋 Tech Stack

- React 18
- Vite 5
- Shadcn/ui (Stone theme)
- Zustand (State management)
- Axios (HTTP client)
- Tailwind CSS
- Lucide Icons
- Bun (Package manager)

## 🛠️ Setup Instructions

### 1. Prerequisites

- Node.js 18+ atau Bun
- Backend API running di `http://localhost:6543`

### 2. Install Bun (jika belum ada)

```bash
# Windows (PowerShell)
powershell -c "irm bun.sh/install.ps1 | iex"
```

### 3. Install Dependencies

```bash
cd frontend
bun install
```

### 4. Run Development Server

```bash
bun run dev
```

Aplikasi akan running di: `http://localhost:5173`

### 5. Build for Production (Optional)

```bash
bun run build
bun run preview
```

## 🎨 UI Components

### Shadcn/ui Components Used

- **Card** - Container untuk content sections
- **Button** - Interactive buttons dengan variants
- **Textarea** - Multi-line input untuk review
- **Badge** - Sentiment indicators
- **Alert** - Error messages display

### Custom Components

#### 1. ThemeToggle
Toggle antara dark dan light mode dengan localStorage persistence.

#### 2. ReviewForm
Form input untuk review dengan:
- Character counter
- Input validation
- Loading state
- Error handling

#### 3. ReviewResults
Display hasil analysis dengan:
- Color-coded sentiment badges (Green/Red/Yellow)
- Confidence score progress bar
- Key points list
- Animated transitions

#### 4. ReviewHistory
List semua reviews dengan:
- Pagination controls
- Formatted timestamps
- Sentiment badges
- Hover effects

## 📂 Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ui/                  # Shadcn components
│   │   │   ├── card.jsx
│   │   │   ├── button.jsx
│   │   │   ├── textarea.jsx
│   │   │   ├── badge.jsx
│   │   │   └── alert.jsx
│   │   ├── ThemeToggle.jsx      # Dark/Light mode toggle
│   │   ├── ReviewForm.jsx       # Review input form
│   │   ├── ReviewResults.jsx    # Analysis results display
│   │   └── ReviewHistory.jsx    # Reviews history list
│   ├── stores/
│   │   └── reviewStore.js       # Zustand state management
│   ├── lib/
│   │   ├── api.js               # Axios API client
│   │   └── utils.js             # Utility functions
│   ├── App.jsx                  # Main app component
│   ├── main.jsx                 # Entry point
│   └── index.css                # Global styles + Tailwind
├── index.html
├── vite.config.js
├── tailwind.config.js
├── components.json              # Shadcn config
└── package.json
```

## 🎨 Theme Configuration

### Stone Theme (Shadcn)

Aplikasi menggunakan **Stone theme** dari Shadcn/ui dengan:
- Neutral color palette
- Professional aesthetics
- Excellent contrast ratios
- Smooth dark mode transitions

### Color Scheme

**Light Mode:**
- Background: `hsl(0 0% 100%)`
- Foreground: `hsl(20 14.3% 4.1%)`

**Dark Mode:**
- Background: `hsl(20 14.3% 4.1%)`
- Foreground: `hsl(60 9.1% 97.8%)`

### Sentiment Colors

- **Positive**: Green (`bg-green-600`)
- **Negative**: Red (`bg-red-600`)
- **Neutral**: Yellow (`bg-yellow-600`)

## 🔄 State Management

### Zustand Store

Store global untuk manage:
- `reviews` - Array of all reviews
- `currentAnalysis` - Latest analysis result
- `isLoading` - Loading state
- `error` - Error messages
- `pagination` - Pagination info

```javascript
import useReviewStore from '@/stores/reviewStore'

// Get state
const { reviews, isLoading } = useReviewStore()

// Update state
const { setLoading, setError } = useReviewStore()
```

## 📡 API Integration

### API Client (`lib/api.js`)

```javascript
import { analyzeReview, getReviews } from '@/lib/api'

// Analyze review
const result = await analyzeReview("Great product!")

// Get reviews with pagination
const data = await getReviews(page, limit)
```

### Error Handling

Semua API calls wrapped dengan try-catch dan menampilkan user-friendly error messages.

## 🎯 Key Features Explained

### 1. Real-time Sentiment Analysis
- User input review → Loading spinner → Display hasil
- Color-coded badges untuk easy identification
- Confidence score dengan progress bar

### 2. Multi-language Support
- Support input dalam bahasa apapun
- Gemini AI otomatis respond dalam bahasa yang sama
- No translation needed

### 3. Dark/Light Mode
- Auto-detect system preference
- Manual toggle dengan smooth transition
- Persistent dengan localStorage

### 4. Responsive Pagination
- 10 items per page (default)
- Previous/Next navigation
- Page counter display

## 🔧 Development

### Available Scripts

```bash
# Start dev server
bun run dev

# Build for production
bun run build

# Preview production build
bun run preview
```

### Adding New Shadcn Components

```bash
bunx shadcn-ui@latest add [component-name]
```

## 🐛 Troubleshooting

### Error: Cannot connect to backend

- Pastikan backend running di `http://localhost:6543`
- Check CORS configuration di backend
- Verify API_BASE_URL di `lib/api.js`

### Error: Module not found

```bash
# Reinstall dependencies
rm -rf node_modules
bun install
```

### Theme not working

- Clear browser localStorage
- Hard refresh (Ctrl + Shift + R)
- Check `index.css` import di `main.jsx`

## 📱 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)

## 📝 Notes

- Default theme: Stone (light mode)
- Auto dark mode based on system preference
- Icons dari Lucide React
- Font: Inter (Google Fonts)

## 🚀 Performance

- Vite for fast HMR
- Code splitting otomatis
- Lazy loading components (optional)
- Optimized build size

## 🔒 Security

- XSS protection with React
- Input sanitization
- HTTPS in production (recommended)

## 📞 Support

Untuk issues atau pertanyaan, silakan buat issue di repository.
