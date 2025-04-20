# db_utils.py
import sqlite3
from datetime import datetime
from io import BytesIO
import pandas as pd

def init_db():
    conn = get_db_connection()  # Use the cached connection
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reports
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 filename TEXT,
                 upload_date TEXT,
                 analysis_text TEXT,
                 file_data BLOB)''')
    conn.commit()

def save_report(filename, analysis_text, file_data):
    """Save a report to the database"""
    conn = sqlite3.connect("financial_reports.db")
    c = conn.cursor()
    
    c.execute("INSERT INTO reports (filename, upload_date, analysis_text, file_data) VALUES (?, ?, ?, ?)",
              (filename, datetime.now().strftime("%Y-%m-%d %H:%M"), analysis_text, file_data))
    
    conn.commit()
    conn.close()
    return True

def load_all_reports():
    """Load all reports (metadata only)"""
    conn = sqlite3.connect("financial_reports.db")
    df = pd.read_sql("SELECT id, filename, upload_date FROM reports ORDER BY upload_date DESC", conn)
    conn.close()
    return df

def load_single_report(report_id):
    """Load a specific report by ID"""
    conn = sqlite3.connect("financial_reports.db")
    c = conn.cursor()
    
    try:
        c.execute("SELECT filename, analysis_text, file_data FROM reports WHERE id=?", (report_id,))
        result = c.fetchone()
        return result
    except Exception as e:
        print(f"Error loading report: {str(e)}")
        return None
    finally:
        conn.close()
