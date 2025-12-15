import sqlite3

def fix_sample_data():
    """Fix The Economist record - remove date for Not Received status."""
    conn = sqlite3.connect('periodicals.db')
    cursor = conn.cursor()
    
    # Update The Economist record to have NULL date since it's Not Received
    cursor.execute('''
        UPDATE periodicals 
        SET date_received = NULL 
        WHERE title = 'The Economist' AND status = 'Not Received'
    ''')
    
    conn.commit()
    conn.close()
    print("Fixed sample data - removed date from 'Not Received' record")

if __name__ == '__main__':
    fix_sample_data()
