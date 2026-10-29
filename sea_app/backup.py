import sqlite3
import os
import json
from datetime import datetime
import shutil

DB_PATH = "sea_users.db"
BACKUP_DIR = "backups"
BACKUP_FILE = os.path.join(BACKUP_DIR, f"sea_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")

def create_backup_dir():
    """Create backups directory if it doesn't exist."""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

def backup_database():
    """Create a backup of the current database."""
    create_backup_dir()

    if os.path.exists(DB_PATH):
        try:
            # Create timestamped backup
            backup_file = os.path.join(BACKUP_DIR, f"sea_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
            shutil.copy2(DB_PATH, backup_file)

            # Keep only last 5 backups
            cleanup_old_backups()

            return True, f"Backup created: {backup_file}"
        except Exception as e:
            return False, f"Backup failed: {str(e)}"
    return False, "No database to backup"

def cleanup_old_backups(keep=5):
    """Keep only the last N backups."""
    create_backup_dir()

    try:
        backups = sorted([f for f in os.listdir(BACKUP_DIR) if f.startswith("sea_backup_")])
        if len(backups) > keep:
            for old_backup in backups[:-keep]:
                os.remove(os.path.join(BACKUP_DIR, old_backup))
    except Exception as e:
        print(f"Cleanup error: {e}")

def restore_database(backup_file_path):
    """Restore database from a backup file."""
    try:
        if not os.path.exists(backup_file_path):
            return False, f"Backup file not found: {backup_file_path}"

        # Backup current database first
        if os.path.exists(DB_PATH):
            backup_database()

        # Restore
        shutil.copy2(backup_file_path, DB_PATH)
        return True, "Database restored successfully!"
    except Exception as e:
        return False, f"Restore failed: {str(e)}"

def export_user_data_to_json():
    """Export all user data to JSON for safety."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Get users
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        # Get questions
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()

        conn.close()

        # Format as JSON
        data = {
            "users": [
                {
                    "name": u[1],
                    "age": u[2],
                    "email": u[3],
                    "created_at": u[4],
                    "last_login": u[5]
                }
                for u in users
            ],
            "questions": [
                {
                    "user_email": q[1],
                    "question": q[2],
                    "response": q[3],
                    "asked_at": q[4]
                }
                for q in questions
            ]
        }

        # Save to file
        export_file = f"sea_data_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(export_file, 'w') as f:
            json.dump(data, f, indent=2)

        return True, f"Data exported to {export_file}"
    except Exception as e:
        return False, f"Export failed: {str(e)}"

def list_backups():
    """List all available backups."""
    create_backup_dir()

    backups = []
    try:
        for file in sorted(os.listdir(BACKUP_DIR)):
            if file.startswith("sea_backup_") and file.endswith(".db"):
                file_path = os.path.join(BACKUP_DIR, file)
                file_size = os.path.getsize(file_path)
                backups.append({
                    "name": file,
                    "path": file_path,
                    "size": file_size
                })
    except Exception as e:
        print(f"Error listing backups: {e}")

    return backups
