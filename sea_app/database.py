import sqlite3
import os
from datetime import datetime

DB_PATH = "sea_users.db"

def init_db():
    """Initialize the database with users table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            question TEXT NOT NULL,
            response TEXT,
            asked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_email) REFERENCES users(email)
        )
    """)

    conn.commit()
    conn.close()

def add_user(name, age, email):
    """Add a new user to the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Allow same email to register again (removed UNIQUE constraint)
        cursor.execute("""
            INSERT INTO users (name, age, email, created_at)
            VALUES (?, ?, ?, ?)
        """, (name, age, email, datetime.now()))

        conn.commit()
        conn.close()
        return True, "Account created successfully!"

    except Exception as e:
        return False, f"Error: {str(e)}"

def get_user(email):
    """Get user data by email (most recent if registered multiple times)."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Get the most recent user registration with this email
        cursor.execute("""
            SELECT name, age, email, created_at
            FROM users
            WHERE email = ?
            ORDER BY created_at DESC
            LIMIT 1
        """, (email,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return {
                "name": result[0],
                "age": result[1],
                "email": result[2],
                "created_at": result[3]
            }
        return None

    except Exception as e:
        print(f"Error getting user: {e}")
        return None

def update_last_login(email):
    """Update last login timestamp for the most recent registration."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Update the most recent user with this email
        cursor.execute("""
            UPDATE users
            SET last_login = ?
            WHERE email = ? AND created_at = (
                SELECT MAX(created_at) FROM users WHERE email = ?
            )
        """, (datetime.now(), email, email))

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error updating login: {e}")

def save_question(email, question, response):
    """Save a question and response to the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO questions (user_email, question, response, asked_at)
            VALUES (?, ?, ?, ?)
        """, (email, question, response, datetime.now()))

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving question: {e}")

def get_user_questions(email, limit=10):
    """Get user's question history."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT question, response, asked_at FROM questions
            WHERE user_email = ?
            ORDER BY asked_at DESC
            LIMIT ?
        """, (email, limit))

        results = cursor.fetchall()
        conn.close()
        return results

    except Exception as e:
        print(f"Error getting questions: {e}")
        return []

def get_all_users():
    """Get all registered users (for admin/backup purposes)."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT email, name, age, created_at FROM users")
        results = cursor.fetchall()
        conn.close()
        return results

    except Exception as e:
        print(f"Error getting users: {e}")
        return []
