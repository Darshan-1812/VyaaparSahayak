# 🚀 Quick Deployment Commands

## Docker Deployment (Local/VPS)

### First Time Setup
```bash
# 1. Configure environment
cp .env.example .env
# Edit .env and add your API keys

# 2. Build and run
docker-compose up -d

# 3. Access application
# Frontend: http://localhost
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Daily Development
```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Restart after code changes
docker-compose restart

# Stop services
docker-compose down

# Complete rebuild
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

---

## Render Deployment

### Method 1: Using render.yaml (Recommended)

```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. On Render.com
# - Click "New +" → "Blueprint"
# - Connect GitHub repository
# - Render detects render.yaml automatically
# - Add environment variables in dashboard:
#   GROQ_API_KEY
#   SERPAPI_KEY

# 3. Done! Render auto-deploys on every push
```

### Method 2: Manual Service Creation

#### Backend
```
Type: Web Service
Name: vyaaparsahayak-backend
Root Directory: backend
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
Environment Variables:
  - GROQ_API_KEY=your_key
  - SERPAPI_KEY=your_key
  - PYTHON_VERSION=3.12.0
```

#### Frontend
```
Type: Static Site
Name: vyaaparsahayak-frontend
Root Directory: frontend
Build Command: npm install && npm run build
Publish Directory: dist
Environment Variables:
  - VITE_API_URL=https://vyaaparsahayak-backend.onrender.com
  - NODE_VERSION=18.17.0
```

---

## Testing Deployment

### Local Docker
```bash
# Backend health check
curl http://localhost:8000/dashboard

# Frontend check
curl http://localhost

# Check running containers
docker ps

# View container logs
docker logs vyaaparsahayak-backend
docker logs vyaaparsahayak-frontend
```

### Render Production
```bash
# Backend health check
curl https://your-backend.onrender.com/dashboard

# Frontend check
curl https://your-frontend.onrender.com

# API documentation
open https://your-backend.onrender.com/docs
```

---

## Troubleshooting

### Docker Issues
```bash
# Container not starting
docker-compose logs backend
docker-compose logs frontend

# Port already in use
# Edit docker-compose.yml and change ports

# Clean everything and restart
docker-compose down -v
docker system prune -a
docker-compose up -d --build
```

### Render Issues
```bash
# Build failing
# Check logs in Render dashboard
# Verify requirements.txt and package.json

# API not connecting
# Check VITE_API_URL environment variable
# Verify CORS settings in backend

# Database resets
# Expected on free tier - use external DB for production
```

---

## Environment Variables

### Root .env (for Docker Compose)
```env
GROQ_API_KEY=your_groq_api_key
SERPAPI_KEY=your_serpapi_key
```

### Backend .env
```env
GROQ_API_KEY=your_groq_api_key
SERPAPI_KEY=your_serpapi_key
```

### Frontend .env (development)
```env
VITE_API_URL=http://127.0.0.1:8000
```

---

## Common Commands

```bash
# View project structure
tree -L 2

# Check Docker status
docker-compose ps

# Follow logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Restart specific service
docker-compose restart backend
docker-compose restart frontend

# Execute command in container
docker-compose exec backend python -c "print('Hello')"

# Clean Docker cache
docker system prune -a --volumes

# Push to production (Render)
git add .
git commit -m "Update"
git push origin main
```

---

## URLs Reference

### Development
- Frontend: http://localhost:8080
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Docker
- Frontend: http://localhost
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Production (Render)
- Frontend: https://your-app.onrender.com
- Backend: https://your-backend.onrender.com
- API Docs: https://your-backend.onrender.com/docs

---

**Need detailed instructions? See [DEPLOYMENT.md](DEPLOYMENT.md)**
