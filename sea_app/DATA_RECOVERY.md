# 🔄 Data Recovery Guide - Sea

If your data was lost after an app update or reset, you can recover it!

## ✅ How Data Backup Works

Sea automatically creates backups:
- 📦 **Automatic backup** every time the app starts
- 💾 **Manual backup** - click the button in Settings
- 📁 **Kept in `/backups/` folder** - up to 5 recent backups
- 🔐 **Stored locally** - completely private

## 🆘 If You Lost Your Account

### Scenario 1: Database Was Deleted

If the `sea_users.db` file was deleted but backups exist:

1. **Open the app**
2. Click **⚙️ Settings** (top right)
3. Click **"📂 View Backups"**
4. See available backups listed
5. (Coming soon) Click "Restore" to recover

### Scenario 2: Re-Register with Same Email

If you can't access a backup, you can **register again with the same email**:

1. Click **Register**
2. Enter your name, age, and **same Gmail address**
3. Click "Register"
4. You're back in! (Note: Your question history won't be there, but your account works)

## 📂 Manual Recovery Steps

### If You Have a Backup File

**Windows PowerShell:**
```powershell
# Find the backup
ls backups/

# Restore it
Copy-Item "backups/sea_backup_YYYYMMDD_HHMMSS.db" "sea_users.db" -Force

# Run the app
streamlit run app.py
```

**macOS/Linux:**
```bash
# Find the backup
ls backups/

# Restore it
cp backups/sea_backup_YYYYMMDD_HHMMSS.db sea_users.db

# Run the app
streamlit run app.py
```

## 🗂️ Backup File Location

All backups are stored in:
```
sea_app/
└── backups/
    ├── sea_backup_20240115_143022.db
    ├── sea_backup_20240115_120500.db
    └── sea_backup_20240114_190330.db
```

## 📊 What Gets Backed Up

✅ **User profiles** - Name, age, email, created date  
✅ **Login history** - Last login timestamp  
✅ **Question history** - All questions and responses  
❌ **API keys** - Never stored or backed up (stored as env variable)  

## 🛡️ Best Practices

1. **Keep backups safe** - Don't delete the `backups/` folder
2. **Export important data** - (Feature coming soon)
3. **Re-register if needed** - Same email can be registered multiple times
4. **Automatic protection** - Backups happen automatically every startup

## ⚠️ Common Issues

### "I registered but still can't login"
- Make sure you're using the **exact same Gmail address**
- Email is case-insensitive (both work): `user@gmail.com` and `USER@GMAIL.COM`
- You might have registered with a typo - try both variations

### "Backup not working"
- Check that `backups/` folder exists
- Make sure you have write permissions in the app folder
- Try creating a manual backup and check if it works

### "I lost everything"
- If you don't have backups, **register again with the same email**
- You'll get a fresh account but keep using the same email
- Your old question history won't be there, but you can start fresh

## 🔄 Recovery Workflow

```
App Resets/Updates
        ↓
❌ Can't login with old account
        ↓
   Try one of these:
        ↓
[Restore from Backup] OR [Re-register with same email]
        ↓
✅ Account is back!
```

---

## 🚀 Coming Soon

- 📥 **Restore button** in Settings (to restore from backup with one click)
- 📤 **Export to JSON** (backup data as text file)
- 📋 **Import from JSON** (restore from text file backup)
- ☁️ **Cloud backup** (optional, encrypted cloud storage)

For now, if you need to restore:
1. Use the manual steps above, OR
2. Re-register with your email

---

**Questions?** Check the main [README.md](README.md) or [FEATURES.md](FEATURES.md)
