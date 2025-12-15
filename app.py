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
    periodicals = conn.execute('SELECT * FROM periodicals ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', periodicals=periodicals)

# Add new record - Display form
@app.route('/add', methods=['GET', 'POST'])
def add_record():
    """Add a new periodical record."""
    if request.method == 'POST':
        # Get form data
        type_val = request.form['type']
        title = request.form['title']
        vendor = request.form['vendor']
        issue_volume = request.form.get('issue_volume', '').strip() or None
        status = request.form['status']
        entered_by = request.form['entered_by']
        notes = request.form.get('notes', '').strip() or None
        
        # Handle date based on status
        if status == 'Received':
            date_received = request.form.get('date_received')
            if not date_received:
                # If no date provided, use today
                from datetime import date
                date_received = date.today().isoformat()
        else:
            date_received = None
        
        # Insert into database
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO periodicals (type, title, vendor, issue_volume, date_received, status, entered_by, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (type_val, title, vendor, issue_volume, date_received, status, entered_by, notes))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    # GET request - show the form
    return render_template('add.html')

# Edit record - Display form and handle update
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_record(id):
    """Edit an existing periodical record."""
    conn = get_db_connection()
    
    if request.method == 'POST':
        # Get form data
        type_val = request.form['type']
        title = request.form['title']
        vendor = request.form['vendor']
        issue_volume = request.form.get('issue_volume', '').strip() or None
        status = request.form['status']
        entered_by = request.form['entered_by']
        notes = request.form.get('notes', '').strip() or None
        
        # Handle date based on status
        if status == 'Received':
            date_received = request.form.get('date_received')
            if not date_received:
                from datetime import date
                date_received = date.today().isoformat()
        else:
            date_received = None
        
        # Update database
        conn.execute('''
            UPDATE periodicals 
            SET type=?, title=?, vendor=?, issue_volume=?, date_received=?, status=?, entered_by=?, notes=?
            WHERE id=?
        ''', (type_val, title, vendor, issue_volume, date_received, status, entered_by, notes, id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    # GET request - fetch existing record and show form
    record = conn.execute('SELECT * FROM periodicals WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if record is None:
        return "Record not found", 404
    
    return render_template('edit.html', record=record)

# Delete record
@app.route('/delete/<int:id>', methods=['POST'])
def delete_record(id):
    """Delete a periodical record."""
    conn = get_db_connection()
    conn.execute('DELETE FROM periodicals WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
