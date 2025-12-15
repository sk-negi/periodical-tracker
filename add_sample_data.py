import sqlite3
from datetime import datetime, timedelta

def add_sample_data():
    """Add sample periodical records for testing."""
    conn = sqlite3.connect('periodicals.db')
    cursor = conn.cursor()
    
    # Sample data - realistic library periodicals
    sample_records = [
        ('Newspaper', 'The Hindu', 'Hindu Group', None, '2024-12-14', 'Received', 'Priya Sharma', None),
        ('Newspaper', 'Times of India', 'Times Group', None, '2024-12-14', 'Received', 'Rajesh Kumar', None),
        ('Periodical', 'Nature Magazine', 'Springer Nature', 'Vol. 624, Issue 7992', '2024-12-13', 'Received', 'Priya Sharma', 'Cover slightly damaged'),
        ('Periodical', 'The Economist', 'The Economist Group', 'December 9th 2024', None, 'Not Received', 'Anjali Verma', 'Vendor notified of delay'),
        ('Newspaper', 'Indian Express', 'Express Group', None, '2024-12-15', 'Received', 'Rajesh Kumar', None),
        ('Periodical', 'Library Trends', 'Johns Hopkins University Press', 'Vol. 72, No. 2', '2024-12-10', 'Received', 'Anjali Verma', None),
    ]
    
    cursor.executemany('''
        INSERT INTO periodicals (type, title, vendor, issue_volume, date_received, status, entered_by, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_records)
    
    conn.commit()
    conn.close()
    print(f"Added {len(sample_records)} sample records successfully!")

if __name__ == '__main__':
    add_sample_data()
