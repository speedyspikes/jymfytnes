from database import create_client

# Function to delete all dummy data from each table
def nuke_data():
    # Connect to the SQLite database
    conn = create_client()
    cursor = conn.cursor()

    # Temporarily disable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

    cursor.execute("DELETE FROM TRAINER")
    cursor.execute("DELETE FROM ROOM")
    cursor.execute("DELETE FROM TRAINER_TrainerSpecialty")
    cursor.execute("DELETE FROM Room_Equipment")
    cursor.execute("DELETE FROM MEMBER")
    cursor.execute("DELETE FROM CLASS")
    cursor.execute("DELETE FROM PERSONAL_TRAINING_SESSION")
    cursor.execute("DELETE FROM Class_Attendance")

    # Re-enable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
    
    conn.commit()
    print("All data deleted successfully.")
    cursor.close()
    conn.close()


if __name__ == "__main__":
  action = input("Are you sure you want to NUKE all data? (y/n): ")
  if action == "y":
      print("Nuking all data")
      nuke_data()
  else:
     print("Nuke aborted")
