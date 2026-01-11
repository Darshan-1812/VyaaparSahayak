# VyaaparSahayak - Project Structure

## 📁 Directory Structure

```
VyaaparSahayak/
│
├── backend/                    # FastAPI Backend
│   ├── main.py                # Main FastAPI application
│   ├── run_server.py          # Server startup script
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # API keys (GROQ, SerpAPI)
│   ├── schemes.json           # Government schemes data
│   └── app.db                 # SQLite database (auto-created)
│
├── frontend/                   # React + Vite Frontend
│   ├── src/                   # Source code
│   │   ├── pages/            # React pages
│   │   ├── components/       # Reusable components
│   │   ├── lib/              # API client & utilities
│   │   └── hooks/            # Custom React hooks
│   ├── public/               # Static assets
│   ├── package.json          # Node dependencies
│   ├── vite.config.ts        # Vite configuration
│   ├── tsconfig.json         # TypeScript config
│   └── tailwind.config.ts    # Tailwind CSS config
│
├── .venv/                     # Python virtual environment
├── .env                       # Root env file (if needed)
├── README.md                  # Project documentation
└── PROJECT_STRUCTURE.md       # This file
```

## 🚀 Quick Start Guide

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Python environment is already configured at project root (.venv)

# Install dependencies (if not already done)
pip install -r requirements.txt

# Start backend server
python run_server.py
```

Backend will run on: **http://127.0.0.1:8000**
API Documentation: **http://127.0.0.1:8000/docs**

### 2. Frontend Setup

Open a **new terminal window** (keep backend running):

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will run on: **http://localhost:8080**

## 🔑 Environment Variables

### Backend `.env` (backend/.env)

```env
# Required for AI features
GROQ_API_KEY=your_groq_api_key_here

# Optional for enhanced market research
SERPAPI_KEY=your_serpapi_key_here
```

## 📦 Key Technologies

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM
- **SQLite** - Lightweight database
- **GROQ** - AI API for risk analysis & content generation
- **Uvicorn** - ASGI server

### Frontend
- **React** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **TailwindCSS** - Styling
- **shadcn/ui** - UI components
- **React Router** - Navigation

## 🛠️ Development Commands

### Backend
```bash
cd backend
python run_server.py          # Start server with auto-reload
```

### Frontend
```bash
cd frontend
npm run dev                   # Start dev server
npm run build                 # Build for production
npm run preview               # Preview production build
```

## 📊 Database

- **Type**: SQLite
- **Location**: `backend/app.db`
- **Auto-created** on first run
- **Tables**: products, orders, production_batches, startup_profiles, schemes, risk_reports

## 🌐 API Endpoints

- `GET /products` - List products
- `POST /products` - Create product
- `POST /orders` - Create order
- `GET /dashboard` - Dashboard metrics
- `POST /ai/audience-matching` - AI audience analysis
- `POST /ai/content-optimization` - AI content generation
- `POST /risk-analysis` - Business risk analysis
- `GET /schemes` - Government schemes

Full API docs: http://127.0.0.1:8000/docs

## 📝 Notes

1. **Backend must run first** before starting frontend
2. **Python virtual environment** (.venv) is at project root
3. **No duplicate files** - each file has a single location
4. **Frontend connects to backend** via http://127.0.0.1:8000
5. **Database is created automatically** on first backend startup

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Windows - Find and kill process
netstat -ano | findstr :8000
taskkill /F /PID <PID>
```

### Frontend Can't Connect
- Ensure backend is running on port 8000
- Check CORS settings in backend/main.py
- Verify API_BASE_URL in frontend/src/lib/api.ts

### Database Issues
```bash
# Delete and recreate
cd backend
rm app.db
python run_server.py  # Will recreate database
```

---

**Ready to build! 🚀**
