import sqlite3

# Function to delete dummy data from each table
def delete_dummy_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('jym.db')
    cursor = conn.cursor()

    try:
        # Delete the dummy data from the TRAINER table
        cursor.execute("DELETE FROM TRAINER WHERE TrainerID IN (1, 2)")

        # Delete the dummy data from the ROOM table
        cursor.execute("DELETE FROM ROOM WHERE RoomNumber IN (101, 102)")

        # Delete the dummy data from the TRAINER_TrainerSpecialty table
        cursor.execute("DELETE FROM TRAINER_TrainerSpecialty WHERE TrainerID IN (1, 2)")

        # Delete the dummy data from the Room_Equipment table
        cursor.execute("DELETE FROM Room_Equipment WHERE RoomNumber IN (101, 102)")

        # Delete the dummy data from the MEMBER table
        cursor.execute("DELETE FROM MEMBER WHERE MemberID IN (1, 2)")

        # Delete the dummy data from the CLASS table
        cursor.execute("DELETE FROM CLASS WHERE ClassID IN (1, 2)")

        # Delete the dummy data from the PERSONAL_TRAINING_SESSION table
        cursor.execute("DELETE FROM PERSONAL_TRAINING_SESSION WHERE SessionID IN (1, 2)")

        # Delete the dummy data from the Class_Attendance table
        cursor.execute("DELETE FROM Class_Attendance WHERE ClassID IN (1, 2)")

        # Commit the transaction
        conn.commit()
        print("Dummy data deleted successfully.")

    except sqlite3.Error as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print("Error occurred:", e)

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Call the function to delete dummy data
delete_dummy_data()
