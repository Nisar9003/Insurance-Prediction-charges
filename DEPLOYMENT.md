# 🚀 Public Deployment Guide

Your app has been updated for public deployment. Here are the easiest options:

---

## **Option 1: Streamlit Cloud + Railway (RECOMMENDED)**

### Step 1: Push to GitHub
1. Create a GitHub account (free)
2. Create a new repository
3. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/fast-api-insurance.git
   git push -u origin main
   ```

### Step 2: Deploy Backend on Railway
1. Go to https://railway.app/
2. Sign up with GitHub
3. Create new project → Import from GitHub
4. Select your repository
5. Add `Procfile` to your repo:
   ```
   web: uvicorn app:app --host 0.0.0.0 --port $PORT
   ```
6. Deploy
7. Copy the public URL (e.g., `https://fast-api-xyz.railway.app`)

### Step 3: Deploy Frontend on Streamlit Cloud
1. Go to https://streamlit.io/cloud
2. Sign in with GitHub
3. Click "New app"
4. Select your repository and choose `frontend.py`
5. In "Advanced settings", add environment variable:
   - Key: `API_URL`
   - Value: `https://fast-api-xyz.railway.app/predict` (your Railway URL)
6. Deploy! ✅

---

## **Option 2: Railway Only (Simple)**
Deploy both frontend and backend on Railway:
- Same process as above
- Add another Streamlit service

---

## **Quick Local Testing**
Before deploying, update `app.py` to allow CORS:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## **Environment Variables (Production)**
When deploying:
- Backend needs: Nothing special (port auto-assigned)
- Frontend needs: `API_URL` = your backend URL

---

**Your app will be public and sharable via link!** 🎉
