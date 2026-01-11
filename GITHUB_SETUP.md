# 📤 GitHub Setup Guide - VyaaparSahayak

Follow these steps to push your project to GitHub.

---

## Step 1: Create GitHub Repository

### 1.1 Go to GitHub
1. Open your browser and go to: https://github.com
2. Sign in to your account (or create one if you don't have it)

### 1.2 Create New Repository
1. Click the **"+"** icon in the top-right corner
2. Select **"New repository"**
3. Fill in the details:
   - **Repository name**: `VyaaparSahayak`
   - **Description**: "AI-powered business intelligence platform for Indian MSMEs and startups"
   - **Visibility**: Choose Public or Private
   - **IMPORTANT**: ❌ **DO NOT** initialize with README, .gitignore, or license
   - (We already have these files)
4. Click **"Create repository"**

### 1.3 Copy Repository URL
After creating, you'll see a page with setup instructions. Copy the repository URL:
- **HTTPS**: `https://github.com/YOUR_USERNAME/VyaaparSahayak.git`
- **SSH**: `git@github.com:YOUR_USERNAME/VyaaparSahayak.git`

**Keep this page open!** You'll need the URL in the next steps.

---

## Step 2: Initialize Git and Push

Open **PowerShell** in your project folder and run these commands:

### 2.1 Navigate to Project Directory
```powershell
cd E:\PROJECT_3rd\VyaaparSahayak
```

### 2.2 Initialize Git (if not already done)
```powershell
git init
```

### 2.3 Configure Git (First time only)
```powershell
# Set your name
git config --global user.name "Your Name"

# Set your email (use your GitHub email)
git config --global user.email "your.email@example.com"
```

### 2.4 Add All Files
```powershell
git add .
```

### 2.5 Create First Commit
```powershell
git commit -m "Initial commit - VyaaparSahayak with Docker and Render deployment"
```

### 2.6 Rename Branch to 'main'
```powershell
git branch -M main
```

### 2.7 Add Remote Repository
**Replace `YOUR_USERNAME` with your actual GitHub username:**
```powershell
git remote add origin https://github.com/YOUR_USERNAME/VyaaparSahayak.git
```

### 2.8 Push to GitHub
```powershell
git push -u origin main
```

**You may be asked to authenticate:**
- **Username**: Your GitHub username
- **Password**: Use a **Personal Access Token** (not your GitHub password)

---

## Step 3: Get GitHub Personal Access Token (If Needed)

If you don't have a token or need a new one:

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Set:
   - **Note**: "VyaaparSahayak Deployment"
   - **Expiration**: 90 days (or your preference)
   - **Select scopes**: Check `repo` (all repo permissions)
4. Click **"Generate token"**
5. **COPY THE TOKEN** - you won't see it again!
6. Use this token as your password when pushing to GitHub

---

## Step 4: Verify Upload

1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/VyaaparSahayak`
2. You should see all your files uploaded
3. Check that:
   - ✅ Backend folder exists
   - ✅ Frontend folder exists
   - ✅ README.md is visible
   - ✅ .env is NOT uploaded (it's in .gitignore)

---

## Quick Command Summary

Here's the complete sequence to copy-paste:

```powershell
# 1. Navigate to project
cd E:\PROJECT_3rd\VyaaparSahayak

# 2. Initialize Git
git init

# 3. Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 4. Add all files
git add .

# 5. Check what will be committed
git status

# 6. Commit
git commit -m "Initial commit - VyaaparSahayak with Docker and Render deployment"

# 7. Rename branch
git branch -M main

# 8. Add remote (REPLACE YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/VyaaparSahayak.git

# 9. Push to GitHub
git push -u origin main
```

---

## Future Updates

After the initial push, when you make changes:

```powershell
# 1. Add changed files
git add .

# 2. Commit with a message
git commit -m "Description of your changes"

# 3. Push to GitHub
git push
```

---

## Troubleshooting

### Error: "fatal: not a git repository"
```powershell
git init
```

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/VyaaparSahayak.git
```

### Error: "failed to push some refs"
```powershell
# Pull first, then push
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Error: "Support for password authentication was removed"
You need to use a Personal Access Token instead of your password:
1. Follow **Step 3** above to create a token
2. Use the token as your password when prompted

### Large files error
```powershell
# Check file sizes
git ls-files -s | sort -k4 -n -r | head -20

# Remove large files from Git
git rm --cached path/to/large/file
echo "path/to/large/file" >> .gitignore
git commit -m "Remove large file"
```

---

## Alternative: Using GitHub Desktop

If you prefer a GUI:

1. Download **GitHub Desktop**: https://desktop.github.com
2. Install and sign in to your GitHub account
3. Click **"Add"** → **"Add existing repository"**
4. Browse to: `E:\PROJECT_3rd\VyaaparSahayak`
5. Click **"Publish repository"**
6. Choose repository name and visibility
7. Click **"Publish repository"**

---

## Next Steps After Pushing

1. **Deploy to Render**:
   - Go to https://render.com
   - Connect your GitHub repository
   - Follow [DEPLOYMENT.md](DEPLOYMENT.md) instructions

2. **Add Repository Badges** (Optional):
   Add to your README.md:
   ```markdown
   ![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/VyaaparSahayak)
   ![GitHub repo size](https://img.shields.io/github/repo-size/YOUR_USERNAME/VyaaparSahayak)
   ```

3. **Set Up GitHub Actions** (Optional):
   - Automate testing and deployment
   - Add CI/CD workflows

---

**Need help? Check the commands above or ask for assistance!** 🚀
