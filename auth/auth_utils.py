import sqlite3
import os
from functools import wraps
from flask import session, redirect, url_for

DB_PATH = os.path.join(os.path.dirname(__file__), '../db/users.db')

def create_user(name, email, interest, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT UNIQUE,
                    interest TEXT,
                    password TEXT,
                    is_paid INTEGER DEFAULT 0
                )''')

    try:
        c.execute("INSERT INTO users (name, email, interest, password) VALUES (?, ?, ?, ?)",
                  (name, email, interest, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def check_user(email, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, email, interest, is_paid FROM users WHERE email = ? AND password = ?", (email, password))
    result = c.fetchone()
    conn.close()

    if result:
        return {
            'name': result[0],
            'email': result[1],
            'interest': result[2],
            'is_paid': result[3]
        }
    return None
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper
# Run as standalone to test DB connection
if __name__ == '__main__':
    test = create_user("Test User", "test@email.com", "Tech", "pass123")
    print("User creation:", test)

    user = check_user("test@email.com", "pass123")
    print("User check:", user)
