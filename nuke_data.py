import sqlite3

# Function to delete all dummy data from each table
def nuke_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('jym.db')
    cursor = conn.cursor()

    try:
        # Delete all data from the TRAINER table
        cursor.execute("DELETE FROM TRAINER")

        # Delete all data from the ROOM table
        cursor.execute("DELETE FROM ROOM")

        # Delete all data from the TRAINER_TrainerSpecialty table
        cursor.execute("DELETE FROM TRAINER_TrainerSpecialty")

        # Delete all data from the Room_Equipment table
        cursor.execute("DELETE FROM Room_Equipment")

        # Delete all data from the MEMBER table
        cursor.execute("DELETE FROM MEMBER")

        # Delete all data from the CLASS table
        cursor.execute("DELETE FROM CLASS")

        # Delete all data from the PERSONAL_TRAINING_SESSION table
        cursor.execute("DELETE FROM PERSONAL_TRAINING_SESSION")

        # Delete all data from the Class_Attendance table
        cursor.execute("DELETE FROM Class_Attendance")

        # Commit the transaction
        conn.commit()
        print("All data deleted successfully.")

    except sqlite3.Error as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print("Error occurred:", e)

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


if __name__ == "__main__":
  nuke_data()
