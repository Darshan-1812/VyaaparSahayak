# 🚀 Deployment Guide - VyaaparSahayak

This guide covers deploying VyaaparSahayak using Docker and Render.com.

---

## 📦 Docker Deployment

### Prerequisites
- Docker installed ([Get Docker](https://www.docker.com/get-started))
- Docker Compose installed (included with Docker Desktop)

### Option 1: Docker Compose (Recommended for Local/VPS)

#### 1. Configure Environment Variables

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API keys
GROQ_API_KEY=your_groq_api_key_here
SERPAPI_KEY=your_serpapi_key_here
```

#### 2. Build and Run

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

#### 3. Access Your Application

- **Frontend**: http://localhost
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### Option 2: Individual Docker Containers

#### Backend

```bash
cd backend

# Build image
docker build -t vyaaparsahayak-backend .

# Run container
docker run -d \
  --name vyaaparsahayak-backend \
  -p 8000:8000 \
  -e GROQ_API_KEY=your_key_here \
  -e SERPAPI_KEY=your_key_here \
  vyaaparsahayak-backend
```

#### Frontend

```bash
cd frontend

# Build image
docker build -t vyaaparsahayak-frontend .

# Run container
docker run -d \
  --name vyaaparsahayak-frontend \
  -p 80:80 \
  vyaaparsahayak-frontend
```

---

## 🌐 Render.com Deployment

Render provides free hosting for web applications with automatic deployments from Git.

### Prerequisites
- GitHub/GitLab account
- Render.com account ([Sign up](https://render.com))

### Step 1: Prepare Your Repository

#### 1.1 Initialize Git (if not already done)

```bash
git init
git add .
git commit -m "Initial commit - Ready for deployment"
```

#### 1.2 Create .gitignore

```bash
# Add to .gitignore
.env
.venv/
__pycache__/
*.pyc
*.db
node_modules/
dist/
.DS_Store
```

#### 1.3 Push to GitHub

```bash
# Create a new repository on GitHub, then:
git remote add origin https://github.com/yourusername/VyaaparSahayak.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render

#### Option A: Using render.yaml (Infrastructure as Code)

1. **Connect Repository**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click **"New +"** → **"Blueprint"**
   - Connect your GitHub repository
   - Render will detect `render.yaml` automatically

2. **Configure Environment Variables**
   - In the Render dashboard, go to each service
   - Add environment variables:
     - `GROQ_API_KEY`: Your GROQ API key
     - `SERPAPI_KEY`: Your SerpAPI key (optional)

3. **Deploy**
   - Render will automatically build and deploy both services
   - Wait for deployment to complete (~5-10 minutes)

#### Option B: Manual Service Creation

##### Deploy Backend

1. **Create Web Service**
   - Click **"New +"** → **"Web Service"**
   - Connect your repository
   - Configure:
     - **Name**: `vyaaparsahayak-backend`
     - **Root Directory**: `backend`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
     - **Plan**: `Free`

2. **Add Environment Variables**
   - Add `GROQ_API_KEY`
   - Add `SERPAPI_KEY` (optional)
   - Add `PYTHON_VERSION`: `3.12.0`

3. **Deploy**
   - Click **"Create Web Service"**
   - Note the service URL: `https://vyaaparsahayak-backend.onrender.com`

##### Deploy Frontend

1. **Create Static Site**
   - Click **"New +"** → **"Static Site"**
   - Connect your repository
   - Configure:
     - **Name**: `vyaaparsahayak-frontend`
     - **Root Directory**: `frontend`
     - **Build Command**: `npm install && npm run build`
     - **Publish Directory**: `dist`

2. **Add Environment Variables**
   - Add `VITE_API_URL`: `https://vyaaparsahayak-backend.onrender.com`
   - Add `NODE_VERSION`: `18.17.0`

3. **Configure Redirects/Rewrites** (in Render dashboard)
   - Add rewrite rule:
     - Source: `/*`
     - Destination: `/index.html`

4. **Deploy**
   - Click **"Create Static Site"**
   - Access your app at: `https://vyaaparsahayak-frontend.onrender.com`

### Step 3: Custom Domain (Optional)

1. Go to your frontend service in Render
2. Click **"Settings"** → **"Custom Domains"**
3. Add your domain
4. Update DNS records as instructed by Render

---

## ⚙️ Environment Variables Reference

### Backend (.env)

```env
# Required
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx

# Optional
SERPAPI_KEY=xxxxxxxxxxxxxxxxxxxxx

# Production (auto-set by Render)
PORT=8000
```

### Frontend (.env)

```env
# Development
VITE_API_URL=http://127.0.0.1:8000

# Production (set in Render)
VITE_API_URL=https://your-backend.onrender.com
```

---

## 🔒 Important Security Notes

### For Production Deployment:

1. **Never commit .env files**
   ```bash
   # Ensure .env is in .gitignore
   echo ".env" >> .gitignore
   ```

2. **Use environment variables in Render**
   - Store all secrets in Render's environment variables
   - Never hardcode API keys in code

3. **Update CORS settings** (backend/main.py)
   ```python
   # For production, restrict origins:
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "https://your-frontend.onrender.com",
           "https://yourdomain.com"
       ],
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

4. **Database Persistence**
   - **Note**: Render's free tier doesn't have persistent storage
   - SQLite database will reset on each deployment
   - For production, consider:
     - Upgrading to Render paid plan
     - Using external database (PostgreSQL, MongoDB)
     - Using Render's managed PostgreSQL

---

## 🎯 Deployment Checklist

### Pre-Deployment

- [ ] All environment variables configured
- [ ] `.gitignore` properly set up
- [ ] Code pushed to GitHub/GitLab
- [ ] GROQ API key obtained
- [ ] Frontend API URL updated for production

### Post-Deployment

- [ ] Backend health check passes
- [ ] Frontend loads correctly
- [ ] API endpoints working
- [ ] Onboarding flow functional
- [ ] AI features working (GROQ API)
- [ ] Database initialized with schemes

---

## 🐛 Troubleshooting

### Docker Issues

**Container won't start:**
```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild from scratch
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

**Port conflicts:**
```bash
# Change ports in docker-compose.yml
ports:
  - "8001:8000"  # Change host port
```

### Render Deployment Issues

**Build failing:**
- Check build logs in Render dashboard
- Verify `requirements.txt` or `package.json` is correct
- Ensure Python/Node version is specified

**API connection failing:**
- Verify `VITE_API_URL` environment variable
- Check CORS settings in backend
- Ensure backend is deployed and running

**Database resets on deploy:**
- This is expected on Render free tier
- Consider upgrading or using external database
- Alternative: Use cloud storage (AWS S3, Cloudinary)

**500 Internal Server Error:**
- Check backend logs in Render dashboard
- Verify environment variables are set
- Check GROQ API key is valid

---

## 📊 Performance Optimization

### Frontend

1. **Enable Gzip** (already configured in nginx.conf)
2. **Use CDN** for static assets
3. **Lazy load** routes and components
4. **Optimize images**

### Backend

1. **Add database indexes**
2. **Implement caching** (Redis)
3. **Use connection pooling**
4. **Rate limiting** for API endpoints

---

## 🚀 Continuous Deployment

Render automatically deploys when you push to your main branch:

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main

# Render automatically:
# 1. Detects changes
# 2. Builds services
# 3. Deploys new version
# 4. Runs health checks
```

---

## 💰 Cost Estimation

### Render Free Tier
- **Backend**: Free (750 hours/month, sleeps after 15 min inactivity)
- **Frontend**: Free (100GB bandwidth/month)
- **Limitations**: 
  - Services sleep when inactive
  - No persistent storage
  - Limited compute resources

### Render Paid Plans (for Production)
- **Starter**: $7/month per service
  - Always-on services
  - More compute resources
  - Better performance
- **Standard**: $25/month per service
  - Persistent storage
  - Auto-scaling
  - Priority support

---

## 📞 Support Resources

- **Render Documentation**: https://render.com/docs
- **Docker Documentation**: https://docs.docker.com
- **FastAPI Deployment**: https://fastapi.tiangolo.com/deployment/
- **Vite Deployment**: https://vitejs.dev/guide/static-deploy

---

## ✅ Success Verification

After deployment, verify:

```bash
# Test backend
curl https://your-backend.onrender.com/dashboard

# Test frontend
curl https://your-frontend.onrender.com

# Check API docs
open https://your-backend.onrender.com/docs
```

---

**Your VyaaparSahayak app is now live! 🎉**

Share your deployed URL and start helping businesses grow!
