import sqlite3

def init_database():
    """Initialize the database and create the periodicals table."""
    conn = sqlite3.connect('periodicals.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS periodicals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            title TEXT NOT NULL,
            vendor TEXT NOT NULL,
            issue_volume TEXT,
            date_received DATE,
            status TEXT NOT NULL,
            entered_by TEXT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == '__main__':
    init_database()
