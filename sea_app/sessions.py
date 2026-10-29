import sqlite3
import os
from datetime import datetime

DB_PATH = "sea_users.db"

def init_sessions_table():
    """Create sessions table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            session_id TEXT NOT NULL,
            question TEXT NOT NULL,
            explanation TEXT,
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ended_at TIMESTAMP,
            questions_count INTEGER DEFAULT 0,
            status TEXT DEFAULT 'active',
            FOREIGN KEY (user_email) REFERENCES users(email)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS session_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            user_email TEXT NOT NULL,
            message_type TEXT,
            content TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_email) REFERENCES users(email)
        )
    """)

    conn.commit()
    conn.close()

def create_new_session(user_email, question):
    """Create a new learning session."""
    import uuid
    session_id = str(uuid.uuid4())[:8]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sessions (user_email, session_id, question, started_at, status)
        VALUES (?, ?, ?, ?, 'active')
    """, (user_email, session_id, question, datetime.now()))

    conn.commit()
    conn.close()

    return session_id

def add_message_to_session(session_id, user_email, message_type, content):
    """Add a message (student answer or Sea response) to session."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO session_messages (session_id, user_email, message_type, content, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (session_id, user_email, message_type, content, datetime.now()))

    conn.commit()
    conn.close()

def end_session(session_id, user_email):
    """Mark session as completed."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Count messages in this session
    cursor.execute("""
        SELECT COUNT(*) FROM session_messages
        WHERE session_id = ? AND user_email = ? AND message_type = 'student'
    """, (session_id, user_email))

    count = cursor.fetchone()[0]

    cursor.execute("""
        UPDATE sessions
        SET ended_at = ?, status = 'completed', questions_count = ?
        WHERE session_id = ? AND user_email = ?
    """, (datetime.now(), count, session_id, user_email))

    conn.commit()
    conn.close()

def get_user_sessions(user_email, limit=20):
    """Get all sessions for a user."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT session_id, question, started_at, ended_at, status, questions_count
        FROM sessions
        WHERE user_email = ?
        ORDER BY started_at DESC
        LIMIT ?
    """, (user_email, limit))

    sessions = cursor.fetchall()
    conn.close()

    return sessions

def get_session_details(session_id, user_email):
    """Get all messages from a specific session."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get session info
    cursor.execute("""
        SELECT session_id, question, started_at, ended_at, status
        FROM sessions
        WHERE session_id = ? AND user_email = ?
    """, (session_id, user_email))

    session_info = cursor.fetchone()

    if not session_info:
        conn.close()
        return None, []

    # Get all messages
    cursor.execute("""
        SELECT message_type, content, timestamp
        FROM session_messages
        WHERE session_id = ? AND user_email = ?
        ORDER BY timestamp ASC
    """, (session_id, user_email))

    messages = cursor.fetchall()
    conn.close()

    return session_info, messages

def get_session_stats(user_email):
    """Get statistics about user's learning sessions."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Total sessions
    cursor.execute("""
        SELECT COUNT(*) FROM sessions WHERE user_email = ?
    """, (user_email,))
    total_sessions = cursor.fetchone()[0]

    # Total questions asked
    cursor.execute("""
        SELECT SUM(questions_count) FROM sessions
        WHERE user_email = ? AND status = 'completed'
    """, (user_email,))

    total_questions = cursor.fetchone()[0] or 0

    # Most recent session
    cursor.execute("""
        SELECT started_at FROM sessions
        WHERE user_email = ?
        ORDER BY started_at DESC
        LIMIT 1
    """, (user_email,))

    last_session = cursor.fetchone()

    conn.close()

    return {
        "total_sessions": total_sessions,
        "total_questions": total_questions,
        "last_session": last_session[0] if last_session else None
    }

def delete_session(session_id, user_email):
    """Delete a session and its messages."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM session_messages
        WHERE session_id = ? AND user_email = ?
    """, (session_id, user_email))

    cursor.execute("""
        DELETE FROM sessions
        WHERE session_id = ? AND user_email = ?
    """, (session_id, user_email))

    conn.commit()
    conn.close()
