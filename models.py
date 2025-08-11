import sqlite3
from datetime import datetime
from config import DB_PATH

def init_db():
    """
    Creates the 'requests_log' table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            operation TEXT,
            input_data TEXT,
            result TEXT
        )
    ''')
    conn.commit()
    conn.close()


def log_request(operation, input_data, result):
    """
    Saves a request to the requests_log table.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat(timespec='seconds')
    
    cursor.execute('''
        INSERT INTO requests_log (timestamp, operation, input_data, result)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, operation, str(input_data), str(result)))
    
    conn.commit()
    conn.close()

def get_all_requests():
    """
    Returns all requests saved in the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, operation, input_data, result FROM requests_log ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    # Converts each row to a dictionary
    result = []
    for row in rows:
        result.append({
            'timestamp': row[0],
            'operation': row[1],
            'input': row[2],
            'result': row[3]
        })
    return result
