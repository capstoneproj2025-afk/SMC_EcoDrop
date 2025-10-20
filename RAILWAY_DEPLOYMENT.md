# 🚂 Railway Deployment Guide for EcoDrop

This guide walks you through deploying your EcoDrop Django application to Railway with automatic superuser creation.

---

## 📋 Prerequisites

- A [Railway account](https://railway.app/) (free tier available)
- Your project pushed to GitHub (Railway deploys from Git repositories)
- Basic familiarity with environment variables

---

## 🚀 Deployment Steps

### Step 1: Create a New Railway Project

1. Go to [Railway.app](https://railway.app/) and log in
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your **SMC_EcoDrop** repository
5. Railway will detect it's a Django project

### Step 2: Add PostgreSQL Database

1. In your Railway project dashboard, click **"+ New"**
2. Select **"Database"** → **"Add PostgreSQL"**
3. Railway will automatically create a PostgreSQL database and set the `DATABASE_URL` environment variable

### Step 3: Configure Environment Variables

Click on your Django service, then go to **"Variables"** tab and add these:

```bash
# Required Variables
DJANGO_SECRET_KEY=your-generated-secret-key-here
DEBUG=False
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@yourdomain.com
DJANGO_SUPERUSER_PASSWORD=YourSecurePassword123!
```

**🔐 Generate a Secret Key:**

Run this command locally to generate a secure secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and use it as your `DJANGO_SECRET_KEY`.

### Step 4: Update CSRF Trusted Origins

After your first deployment, Railway will assign you a domain like:
```
https://your-app-name.up.railway.app
```

**Update `settings.py`:**

```python
CSRF_TRUSTED_ORIGINS = [
    'https://your-app-name.up.railway.app',  # Add your Railway domain
    'https://ecodrop.ccshub.uk',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

ALLOWED_HOSTS = ['your-app-name.up.railway.app', '*']
```

Push this change to trigger a redeploy.

### Step 5: Deploy!

1. Railway will automatically start deploying
2. Watch the **"Deployments"** tab for build logs
3. The build script will:
   - Install dependencies
   - Collect static files
   - Run migrations
   - **Automatically create the superuser** 🎉

### Step 6: Verify Deployment

Once deployed (usually takes 2-5 minutes):

1. Click on your service → **"Settings"** → find your public URL
2. Visit `https://your-app-name.up.railway.app`
3. Go to `/admin` and log in with your superuser credentials

---

## 🔧 Important Files Created

| File | Purpose |
|------|---------|
| `Procfile` | Tells Railway how to start your app (using Gunicorn) |
| `runtime.txt` | Specifies Python version (3.11.0) |
| `railway.json` | Railway-specific build and deployment configuration |
| `build.sh` | Build script that creates superuser automatically |
| `requirements.txt` | Updated with production dependencies |

---

## 🛠️ Build Script Details

The `build.sh` script automatically:

1. ✅ Installs Python dependencies
2. ✅ Collects static files with Whitenoise
3. ✅ Runs database migrations
4. ✅ **Creates superuser** using environment variables
5. ✅ Checks if superuser already exists (idempotent)

**Environment Variables Used:**
- `DJANGO_SUPERUSER_USERNAME` (default: `admin`)
- `DJANGO_SUPERUSER_EMAIL` (default: `admin@ecodrop.com`)
- `DJANGO_SUPERUSER_PASSWORD` (default: `admin123` - **CHANGE THIS!**)

---

## 🎯 Custom Superuser Credentials

You can customize the superuser by setting these environment variables in Railway:

```bash
DJANGO_SUPERUSER_USERNAME=myadmin
DJANGO_SUPERUSER_EMAIL=admin@mycompany.com
DJANGO_SUPERUSER_PASSWORD=MySecurePass123!
```

The build script will use these values when creating the superuser.

---

## 📊 Database Configuration

The app automatically detects the environment:

- **Production (Railway):** Uses PostgreSQL via `DATABASE_URL`
- **Development (Local):** Uses SQLite (`db.sqlite3`)

No manual configuration needed! ✨

---

## 🌐 Static Files

Static files are served using **Whitenoise**, which:
- Compresses files for faster loading
- Serves files directly from Django (no separate CDN needed)
- Works seamlessly on Railway

---

## 🐛 Troubleshooting

### Build Fails

**Check these logs in Railway:**
1. Go to **"Deployments"** tab
2. Click on the failed deployment
3. Read the build logs for errors

**Common issues:**
- Missing environment variables → Check Variables tab
- Database connection → Ensure PostgreSQL service is running
- Static files → Check `build.sh` ran successfully

### Superuser Not Created

If superuser creation fails:

1. SSH into Railway (click **"..."** → **"SSH"**)
2. Run manually:
```bash
python manage.py createsuperuser
```

### Can't Access Admin Panel

1. Check your `ALLOWED_HOSTS` includes your Railway domain
2. Check `CSRF_TRUSTED_ORIGINS` includes `https://your-domain.up.railway.app`
3. Try accessing `/admin` (note the trailing slash)

### Application Error 500

1. Check Railway logs: **"Deployments"** → **"View Logs"**
2. Ensure `DEBUG=False` in production
3. Verify database migrations ran: check build logs

---

## 🔒 Security Best Practices

✅ **DO:**
- Use a strong `DJANGO_SECRET_KEY` (generated, not manual)
- Set `DEBUG=False` in production
- Use strong superuser passwords
- Keep environment variables secret

❌ **DON'T:**
- Commit `.env` files to Git
- Use default passwords like `admin123`
- Enable DEBUG in production
- Hardcode secrets in `settings.py`

---

## 🔄 Redeployment

Every time you push to your GitHub repository:
1. Railway automatically detects the push
2. Runs `build.sh` again
3. Restarts your application
4. Superuser creation is **idempotent** (won't create duplicates)

---

## 📞 Need Help?

- [Railway Documentation](https://docs.railway.app/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- Check Railway community forums

---

## ✅ Deployment Checklist

Before deploying, ensure:

- [ ] All code pushed to GitHub
- [ ] `DJANGO_SECRET_KEY` generated and added to Railway
- [ ] `DEBUG=False` set in Railway
- [ ] Superuser credentials configured
- [ ] PostgreSQL database added to project
- [ ] CSRF_TRUSTED_ORIGINS updated with Railway domain
- [ ] Static files directory exists (`static/`)

---

**🎉 Congratulations! Your EcoDrop app is now live on Railway with an auto-generated admin account!**

Access your admin panel at: `https://your-app-name.up.railway.app/admin`
