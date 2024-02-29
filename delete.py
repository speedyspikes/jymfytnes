# Function to delete data from the database
def delete_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # SQL DELETE statement
    sql_delete = """
        DELETE FROM students
        WHERE name = ?
    """
    # Name of the student to delete
    name_to_delete = 'John Doe'
    try:
        # Execute the DELETE statement
        cursor.execute(sql_delete, (name_to_delete,))
        # Commit the transaction
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print("Error occurred:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
  delete_data()
