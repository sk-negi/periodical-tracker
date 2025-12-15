from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database helper function
def get_db_connection():
    """Create a database connection."""
    conn = sqlite3.connect('periodicals.db')
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

# Homepage - Display all records
@app.route('/')
def index():
    """Display all periodical records."""
    conn = get_db_connection()
    periodicals = conn.execute('SELECT * FROM periodicals ORDER BY date_received DESC').fetchall()
    conn.close()
    return render_template('index.html', periodicals=periodicals)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
