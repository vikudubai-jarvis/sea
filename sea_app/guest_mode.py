import json
import os
from datetime import datetime, timedelta

GUEST_FILE = "guest_session.json"

def load_guest_session():
    """Load guest session data."""
    if os.path.exists(GUEST_FILE):
        try:
            with open(GUEST_FILE, 'r') as f:
                return json.load(f)
        except:
            return None
    return None

def create_guest_session():
    """Create a new guest session with 1 month of free usage."""
    session = {
        "guest_id": "guest_user",
        "created_at": datetime.now().isoformat(),
        "expires_at": (datetime.now() + timedelta(days=30)).isoformat(),
        "locked_out": False,
        "usage_count": 0
    }
    save_guest_session(session)
    return session

def save_guest_session(session):
    """Save guest session data."""
    with open(GUEST_FILE, 'w') as f:
        json.dump(session, f, indent=2)

def is_guest_trial_active():
    """Check if guest free trial (1 month) is still active."""
    session = load_guest_session()
    if not session:
        return True  # First time, create one

    # Check if locked out
    if session.get('locked_out', False):
        return False

    expires_at = datetime.fromisoformat(session['expires_at'])
    return datetime.now() < expires_at

def get_guest_info():
    """Get guest session info."""
    session = load_guest_session()
    if not session:
        session = create_guest_session()

    if session.get('locked_out', False):
        return {
            "guest_id": "Guest User",
            "status": "LOCKED_OUT",
            "message": "Your 1-month free trial has ended. Please login to continue.",
            "locked_out": True
        }

    expires_at = datetime.fromisoformat(session['expires_at'])
    days_left = (expires_at - datetime.now()).days
    hours_left = ((expires_at - datetime.now()).total_seconds() % 86400) / 3600

    if days_left < 0:
        # Trial expired, lock them out
        session['locked_out'] = True
        save_guest_session(session)
        return {
            "guest_id": "Guest User",
            "status": "LOCKED_OUT",
            "message": "Your 1-month free trial has ended. Please login to continue.",
            "locked_out": True
        }

    return {
        "guest_id": "Guest User",
        "status": "ACTIVE",
        "days_left": max(0, days_left),
        "hours_left": round(hours_left, 1),
        "usage_count": session['usage_count'],
        "locked_out": False
    }

def record_guest_usage():
    """Record that guest made a question/learning session."""
    session = load_guest_session()
    if not session:
        session = create_guest_session()

    session['usage_count'] += 1
    save_guest_session(session)

def reset_guest_session():
    """Reset/clear guest session."""
    if os.path.exists(GUEST_FILE):
        os.remove(GUEST_FILE)

def check_trial_expired():
    """Check if trial is expired and return true if so."""
    session = load_guest_session()
    if not session:
        return False

    if session.get('locked_out', False):
        return True

    expires_at = datetime.fromisoformat(session['expires_at'])
    if datetime.now() >= expires_at:
        session['locked_out'] = True
        save_guest_session(session)
        return True

    return False
