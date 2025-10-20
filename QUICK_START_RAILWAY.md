# ⚡ Quick Start: Deploy to Railway in 5 Minutes

## Step 1: Push to GitHub
```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

## Step 2: Create Railway Project
1. Go to https://railway.app/new
2. Click "Deploy from GitHub repo"
3. Select **SMC_EcoDrop**

## Step 3: Add PostgreSQL
1. Click "+ New" → "Database" → "PostgreSQL"

## Step 4: Set Environment Variables

Click your Django service → "Variables" → Add these:

```
DJANGO_SECRET_KEY=<run generate_secret_key.py to get this>
DEBUG=False
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@ecodrop.com
DJANGO_SUPERUSER_PASSWORD=YourSecurePassword123
```

## Step 5: Generate Secret Key

Run locally:
```bash
python generate_secret_key.py
```

Copy the output and paste it as `DJANGO_SECRET_KEY` in Railway.

## Step 6: Deploy & Wait

Railway will:
- ✅ Install dependencies
- ✅ Run migrations
- ✅ Create your superuser automatically
- ✅ Deploy your app

**Done in ~3-5 minutes!** 🎉

Access admin at: `https://your-app.up.railway.app/admin`

---

## 🔄 Update After First Deploy

After you get your Railway URL (e.g., `your-app.up.railway.app`):

1. Update `ecodrop_project/settings.py`:
   ```python
   CSRF_TRUSTED_ORIGINS = [
       'https://your-app.up.railway.app',  # Add this line
       # ... rest stays the same
   ]
   ```

2. Push changes:
   ```bash
   git add .
   git commit -m "Add Railway domain to CSRF origins"
   git push
   ```

Railway will automatically redeploy!

---

## 📝 Login Credentials

**Admin Panel:** `https://your-app.up.railway.app/admin`

- **Username:** Value from `DJANGO_SUPERUSER_USERNAME` (default: `admin`)
- **Password:** Value from `DJANGO_SUPERUSER_PASSWORD`

---

## 🆘 Troubleshooting

### "DisallowedHost" error?
→ Update `ALLOWED_HOSTS` in settings.py with your Railway domain

### "CSRF verification failed"?
→ Add your Railway domain to `CSRF_TRUSTED_ORIGINS`

### Can't log in to admin?
→ Check your superuser credentials match what you set in Railway Variables

### Build failed?
→ Check "Deployments" → "View Logs" in Railway dashboard

---

**Need detailed instructions?** See `RAILWAY_DEPLOYMENT.md`
