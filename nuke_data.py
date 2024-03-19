import mysql.connector as mysql

# Function to delete all dummy data from each table
def nuke_data():
    # Connect to the SQLite database
    conn = mysql.connect('jym.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM TRAINER")
    cursor.execute("DELETE FROM ROOM")
    cursor.execute("DELETE FROM TRAINER_TrainerSpecialty")
    cursor.execute("DELETE FROM Room_Equipment")
    cursor.execute("DELETE FROM MEMBER")
    cursor.execute("DELETE FROM CLASS")
    cursor.execute("DELETE FROM PERSONAL_TRAINING_SESSION")
    cursor.execute("DELETE FROM Class_Attendance")
    
    conn.commit()
    print("All data deleted successfully.")
    cursor.close()
    conn.close()


if __name__ == "__main__":
  nuke_data()
