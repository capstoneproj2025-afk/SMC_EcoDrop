# ✅ Railway Deployment Checklist

Use this checklist to ensure a smooth deployment to Railway.

---

## 📋 Pre-Deployment (Do This First)

### 1. Code Preparation
- [ ] All changes committed to Git
- [ ] Project pushed to GitHub
- [ ] `.gitignore` excludes sensitive files (`.env`, `db.sqlite3`, etc.)
- [ ] No hardcoded secrets in code

### 2. Generate Secret Key
```bash
python generate_secret_key.py
```
- [ ] Secret key generated
- [ ] Secret key copied (keep it safe!)

### 3. Plan Superuser Credentials
Write down your desired credentials:
- [ ] Username: `___________________`
- [ ] Email: `___________________`
- [ ] Password: `___________________` (make it strong!)

---

## 🚂 Railway Setup

### 4. Create Railway Account
- [ ] Signed up at https://railway.app
- [ ] GitHub account connected to Railway

### 5. Create New Project
- [ ] Clicked "New Project"
- [ ] Selected "Deploy from GitHub repo"
- [ ] Chose `SMC_EcoDrop` repository
- [ ] Railway detected Django project ✅

### 6. Add PostgreSQL Database
- [ ] Clicked "+ New" in project
- [ ] Selected "Database" → "PostgreSQL"
- [ ] Database provisioned successfully
- [ ] `DATABASE_URL` automatically set ✅

---

## ⚙️ Environment Variables

### 7. Configure Variables

Go to your Django service → **Variables** tab and add:

#### Required Variables
- [ ] `DJANGO_SECRET_KEY` = `<paste your generated key>`
- [ ] `DEBUG` = `False`
- [ ] `DJANGO_SUPERUSER_USERNAME` = `<your username>`
- [ ] `DJANGO_SUPERUSER_EMAIL` = `<your email>`
- [ ] `DJANGO_SUPERUSER_PASSWORD` = `<your password>`

#### Verify Auto-Set Variables
- [ ] `DATABASE_URL` exists (set by PostgreSQL service)
- [ ] `PORT` exists (set by Railway)

---

## 🚀 First Deployment

### 8. Initial Deploy
- [ ] Clicked "Deploy" or waited for auto-deploy
- [ ] Watched deployment logs in "Deployments" tab
- [ ] Build completed successfully (green checkmark)
- [ ] No errors in logs

### 9. Verify Build Steps
Check logs show:
- [ ] ✅ "Installing Python dependencies..."
- [ ] ✅ "Collecting static files..."
- [ ] ✅ "Running database migrations..."
- [ ] ✅ "Superuser created successfully!" or "Superuser already exists"
- [ ] ✅ "Build complete!"

### 10. Get Your URL
- [ ] Deployment succeeded
- [ ] Copied Railway URL (e.g., `your-app.up.railway.app`)

---

## 🔧 Post-Deployment Configuration

### 11. Update Django Settings

Edit `ecodrop_project/settings.py`:

```python
CSRF_TRUSTED_ORIGINS = [
    'https://your-app.up.railway.app',  # ← Add your Railway URL here
    'https://ecodrop.ccshub.uk',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

ALLOWED_HOSTS = ['your-app.up.railway.app', '*']  # ← Add your domain
```

- [ ] Updated `CSRF_TRUSTED_ORIGINS` with Railway URL
- [ ] Updated `ALLOWED_HOSTS` with Railway URL
- [ ] Changes committed and pushed to GitHub

### 12. Wait for Redeploy
- [ ] Railway auto-detected push
- [ ] Redeploy completed successfully

---

## ✅ Verification

### 13. Test Your Deployment

Visit your Railway URL:

#### Main Application
- [ ] `https://your-app.up.railway.app/` loads
- [ ] No "DisallowedHost" error
- [ ] No "CSRF verification failed" error

#### Admin Panel
- [ ] `https://your-app.up.railway.app/admin` loads
- [ ] Admin login page displays correctly
- [ ] Can log in with superuser credentials
- [ ] Admin dashboard loads properly

#### Dashboard
- [ ] `https://your-app.up.railway.app/dashboard/` accessible
- [ ] Pages render correctly
- [ ] No 500 errors

### 14. Check Database
- [ ] Migrations applied (check Railway logs)
- [ ] Superuser created and can log in
- [ ] Can create/edit data in admin panel

### 15. Verify Static Files
- [ ] CSS loading correctly
- [ ] Images displaying
- [ ] No 404 errors for static files

---

## 🎯 Optional: Custom Domain

### 16. Add Custom Domain (Optional)

If you have a custom domain:

- [ ] Added domain in Railway settings
- [ ] Updated DNS records
- [ ] Domain verified
- [ ] Updated `CSRF_TRUSTED_ORIGINS` with custom domain
- [ ] Updated `ALLOWED_HOSTS` with custom domain

---

## 🛠️ Troubleshooting

### If Build Fails:
1. [ ] Check Railway deployment logs
2. [ ] Verify all environment variables are set
3. [ ] Check for typos in variable names
4. [ ] Ensure PostgreSQL service is running
5. [ ] Review error messages in logs

### If Admin Login Fails:
1. [ ] Verify superuser credentials in environment variables
2. [ ] Check Railway logs for "Superuser created" message
3. [ ] Try resetting password via Railway shell
4. [ ] Verify database migrations ran

### If Static Files Don't Load:
1. [ ] Check `collectstatic` ran in build logs
2. [ ] Verify Whitenoise in `MIDDLEWARE` (settings.py)
3. [ ] Check browser console for errors
4. [ ] Clear browser cache

### If CSRF Errors:
1. [ ] Verify Railway URL in `CSRF_TRUSTED_ORIGINS`
2. [ ] Include `https://` protocol
3. [ ] Push changes and redeploy
4. [ ] Clear browser cookies

---

## 📞 Get Help

### Railway Issues:
- Railway Dashboard → "Deployments" → "View Logs"
- Railway Community: https://help.railway.app
- Railway Discord: https://discord.gg/railway

### Django Issues:
- Check application logs in Railway
- Review Django documentation
- See `RAILWAY_DEPLOYMENT.md` troubleshooting section

---

## 🎉 Success Criteria

Your deployment is successful when:

- ✅ Application loads without errors
- ✅ Admin panel accessible
- ✅ Can log in with superuser account
- ✅ Database connected and working
- ✅ Static files loading correctly
- ✅ No console errors in browser
- ✅ CSRF protection working
- ✅ Can create/modify data

---

## 🔄 Future Deployments

For future updates:

1. [ ] Make code changes locally
2. [ ] Test changes locally
3. [ ] Commit and push to GitHub
4. [ ] Railway auto-deploys (no manual steps!)
5. [ ] Verify deployment in Railway logs
6. [ ] Test changes on live site

---

## 📝 Notes

Use this space to track your deployment details:

**Railway URL:** `_______________________________________________`

**Superuser Username:** `_______________________________________________`

**Database Name:** `_______________________________________________`

**Deployment Date:** `_______________________________________________`

**Custom Domain (if any):** `_______________________________________________`

---

**Status:** 
- [ ] 🟡 In Progress
- [ ] 🟢 Successfully Deployed
- [ ] 🔴 Issues Found (see troubleshooting)

---

*Keep this checklist for future reference and updates!*
