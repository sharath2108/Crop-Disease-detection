import sqlite3
import random
import string
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config import DB_PATH

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def generate_user_id():
    """Generates a human-friendly unique User ID like AGRI-USER-7492"""
    num_part = ''.join(random.choices(string.digits, k=5))
    return f"AGRI-USER-{num_part}"

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            farm_location TEXT DEFAULT 'Farm Estate',
            crop_interests TEXT DEFAULT 'Tomato, Potato, Corn, Apple',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Diagnoses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diagnoses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            image_filename TEXT NOT NULL,
            predicted_class TEXT NOT NULL,
            crop_name TEXT NOT NULL,
            condition_name TEXT NOT NULL,
            confidence REAL NOT NULL,
            severity TEXT NOT NULL,
            similarity_score REAL DEFAULT 0.0,
            reference_image TEXT DEFAULT '',
            notes TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    ''')
    
    conn.commit()
    conn.close()

def register_user(username, full_name, email, password, farm_location="Farm Estate", crop_interests="Tomato, Potato, Apple"):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if username or email already exists
    cursor.execute("SELECT id FROM users WHERE username = ? OR email = ?", (username, email))
    if cursor.fetchone():
        conn.close()
        return None, "Username or Email already registered."
    
    # Generate unique user_id
    while True:
        user_id = generate_user_id()
        cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        if not cursor.fetchone():
            break
            
    hashed = generate_password_hash(password)
    try:
        cursor.execute('''
            INSERT INTO users (user_id, username, full_name, email, password_hash, farm_location, crop_interests)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, username, full_name, email, hashed, farm_location, crop_interests))
        conn.commit()
        conn.close()
        return user_id, None
    except Exception as e:
        conn.close()
        return None, str(e)

def authenticate_user(identifier, password):
    """Allows login via Username or User ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users 
        WHERE username = ? OR user_id = ? OR email = ?
    ''', (identifier, identifier, identifier))
    user = cursor.fetchone()
    conn.close()
    
    if user and check_password_hash(user['password_hash'], password):
        return dict(user)
    return None

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

def save_diagnosis(user_id, image_filename, predicted_class, crop_name, condition_name, confidence, severity, similarity_score=0.0, reference_image="", notes=""):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO diagnoses (
            user_id, image_filename, predicted_class, crop_name, condition_name, 
            confidence, severity, similarity_score, reference_image, notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, image_filename, predicted_class, crop_name, condition_name, confidence, severity, similarity_score, reference_image, notes))
    diag_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return diag_id

def get_user_diagnoses(user_id, limit=50):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM diagnoses 
        WHERE user_id = ? 
        ORDER BY created_at DESC 
        LIMIT ?
    ''', (user_id, limit))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_diagnosis_by_id(diag_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diagnoses WHERE id = ?", (diag_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_analytics_summary(user_id=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if user_id:
        cursor.execute("SELECT COUNT(*) as total FROM diagnoses WHERE user_id = ?", (user_id,))
        total = cursor.fetchone()['total']
        
        cursor.execute("SELECT COUNT(*) as healthy FROM diagnoses WHERE user_id = ? AND LOWER(condition_name) LIKE '%healthy%'", (user_id,))
        healthy = cursor.fetchone()['healthy']
        
        cursor.execute('''
            SELECT predicted_class, COUNT(*) as count 
            FROM diagnoses 
            WHERE user_id = ? 
            GROUP BY predicted_class 
            ORDER BY count DESC 
            LIMIT 5
        ''', (user_id,))
        top_diseases = [dict(r) for r in cursor.fetchall()]
    else:
        cursor.execute("SELECT COUNT(*) as total FROM diagnoses")
        total = cursor.fetchone()['total']
        
        cursor.execute("SELECT COUNT(*) as healthy FROM diagnoses WHERE LOWER(condition_name) LIKE '%healthy%'")
        healthy = cursor.fetchone()['healthy']
        
        cursor.execute('''
            SELECT predicted_class, COUNT(*) as count 
            FROM diagnoses 
            GROUP BY predicted_class 
            ORDER BY count DESC 
            LIMIT 5
        ''', (user_id,))
        top_diseases = [dict(r) for r in cursor.fetchall()]
        
    conn.close()
    infected = total - healthy
    healthy_pct = round((healthy / total * 100), 1) if total > 0 else 0
    
    return {
        "total_scans": total,
        "healthy_count": healthy,
        "infected_count": infected,
        "healthy_percentage": healthy_pct,
        "top_diseases": top_diseases
    }

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
