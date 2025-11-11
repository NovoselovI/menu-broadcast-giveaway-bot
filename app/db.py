
import sqlite3

DB_PATH = "users.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT
            )
        """)
    init_participants_table()

def save_user(user_id: int, username: str = None, first_name: str = None):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT OR REPLACE INTO users (user_id, username, first_name)
            VALUES (?, ?, ?)
        """, (user_id, username, first_name))

def get_all_users():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT user_id FROM users")
        return [row[0] for row in cursor.fetchall()]


def init_participants_table():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS participants (
                user_id INTEGER PRIMARY KEY
            )
        """)

def save_participant(user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT OR IGNORE INTO participants (user_id) VALUES (?)", (user_id,))

def get_all_participants():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT user_id FROM participants")
        return [row[0] for row in cursor.fetchall()]

def get_participant_full(user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("""
            SELECT username, first_name FROM users WHERE user_id = ?
        """, (user_id,))
        return cursor.fetchone()

def clear_participants():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM participants")


