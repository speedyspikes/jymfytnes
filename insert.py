# INSERT data into a table
import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define your SQL INSERT statement
sql_insert = """
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
"""

# Define the data to be inserted
student_data = ('John Doe', 18, 'A')

try:
    # Execute the INSERT statement
    cursor.execute(sql_insert, student_data)
    
    # Commit the transaction
    conn.commit()
    
    print("Record inserted successfully.")

except sqlite3.Error as e:
    # Rollback the transaction if an error occurs
    conn.rollback()
    print("Error occurred:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
