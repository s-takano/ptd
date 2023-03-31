import sqlite3
import hashlib


table_name = "Freee_Deals"
field_name = "credit_partner"

def anonymise(cursor, table_name, field_name):
    # Connect to the database
    conn = sqlite3.connect('dev_db.sqlite3')
    cursor = conn.cursor()
    
    # Select the records from the table
    cursor.execute(f'SELECT id, {field_name} FROM {table_name}')
    rows = cursor.fetchall()

    # Iterate through the rows, compute the SHA-256 hash, and update the table
    for row in rows:
        value_hash = hashlib.sha1(row[1].encode('utf-8')).hexdigest()
        print((row[0], row[1], value_hash))
        cursor.execute(f'UPDATE {table_name} SET {field_name} = ? WHERE id = ?', (value_hash, row[0]))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
