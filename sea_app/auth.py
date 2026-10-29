from database import add_user, get_user, update_last_login
import re

def validate_email(email):
    """Validate Gmail address format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email) is not None

def validate_name(name):
    """Validate name - should be at least 2 characters."""
    return len(name.strip()) >= 2

def validate_age(age):
    """Validate age is within acceptable range."""
    return 3 <= age <= 99

def register_user(name, age, email):
    """Register a new user."""

    # Validation
    if not validate_name(name):
        return False, "Name must be at least 2 characters."

    if not validate_age(age):
        return False, "Age must be between 3 and 99."

    if not validate_email(email):
        return False, "Please use a valid Gmail address (e.g., name@gmail.com)."

    # Add to database
    return add_user(name, age, email)

def check_login(email):
    """Check if user exists and return their data."""

    if not validate_email(email):
        return None

    user_data = get_user(email)

    if user_data:
        update_last_login(email)

    return user_data

def login_user(email):
    """Login user by email."""
    return check_login(email)
