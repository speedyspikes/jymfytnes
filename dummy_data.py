import mysql.connector as mysql

# Function to insert dummy data into each table
def insert_dummy_data():
    # Connect to the SQLite database
    conn = mysql.connect('jym.db')
    cursor = conn.cursor()

    # Insert dummy data into the TRAINER table
    sql_insert_trainer = """
        INSERT INTO TRAINER (TrainerID, TrainerSSN, TrainerEmail, TrainerName, TrainerPhone, TrainerGender)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql_insert_trainer, (1, '123456789', 'trainer1@example.com', 'John Doe', '1234567890', 1))
    cursor.execute(sql_insert_trainer, (2, '987654321', 'trainer2@example.com', 'Jane Smith', '0987654321', 2))

    # Insert dummy data into the ROOM table
    sql_insert_room = """
        INSERT INTO ROOM (RoomNumber)
        VALUES (?)
    """
    cursor.execute(sql_insert_room, (101,))
    cursor.execute(sql_insert_room, (102,))

    # Insert dummy data into the TRAINER_TrainerSpecialty table
    sql_insert_trainer_specialty = """
        INSERT INTO TRAINER_TrainerSpecialty (TrainerSpecialty, TrainerID)
        VALUES (?, ?)
    """
    cursor.execute(sql_insert_trainer_specialty, ('Weightlifting', 1))
    cursor.execute(sql_insert_trainer_specialty, ('Yoga', 2))

    # Insert dummy data into the Room_Equipment table
    sql_insert_room_equipment = """
        INSERT INTO Room_Equipment (RoomEquipment, RoomNumber)
        VALUES (?, ?)
    """
    cursor.execute(sql_insert_room_equipment, ('Dumbbells', 101))
    cursor.execute(sql_insert_room_equipment, ('Yoga Mats', 102))

    # Insert dummy data into the MEMBER table
    sql_insert_member = """
        INSERT INTO MEMBER (MemberEmail, MembershipTier, MemberPhone, MemberName, MemberID, MemberGender, RoomNumber)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql_insert_member, ('member1@example.com', 1, '1111111111', 'Alice Johnson', 1, 2, 101))
    cursor.execute(sql_insert_member, ('member2@example.com', 2, '2222222222', 'Bob Smith', 2, 1, 102))

    # Insert dummy data into the CLASS table
    sql_insert_class = """
        INSERT INTO CLASS (ClassID, ClassName, ClassTime, ClassDayOfWeek, ClassNumberMembers, ClassType, RoomNumber, TrainerID)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql_insert_class, (1, 'Yoga Class', '0900', 1, 10, 'Yoga', 102, 2))
    cursor.execute(sql_insert_class, (2, 'Weightlifting Class', '1100', 3, 8, 'Weightlifting', 101, 1))

    # Insert dummy data into the PERSONAL_TRAINING_SESSION table
    sql_insert_personal_training_session = """
        INSERT INTO PERSONAL_TRAINING_SESSION (SessionDayOfWeek, SessionTime, SessionID, SessionType, MemberID, RoomNumber, TrainerID)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql_insert_personal_training_session, (2, '1300', 1, 'Weightlifting', 1, 101, 1))
    cursor.execute(sql_insert_personal_training_session, (4, '1500', 2, 'Yoga', 2, 102, 2))

    # Insert dummy data into the Class_Attendance table
    sql_insert_class_attendance = """
        INSERT INTO Class_Attendance (ClassID, MemberID)
        VALUES (?, ?)
    """
    cursor.execute(sql_insert_class_attendance, (1, 1))
    cursor.execute(sql_insert_class_attendance, (2, 2))

    conn.commit()
    print("Dummy data inserted successfully.")

    cursor.close()
    conn.close()


# Function to delete dummy data from each table
def delete_dummy_data():
    # Connect to the SQLite database
    conn = mysql.connect('jym.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM TRAINER WHERE TrainerID IN (1, 2)")
    cursor.execute("DELETE FROM ROOM WHERE RoomNumber IN (101, 102)")
    cursor.execute("DELETE FROM TRAINER_TrainerSpecialty WHERE TrainerID IN (1, 2)")
    cursor.execute("DELETE FROM Room_Equipment WHERE RoomNumber IN (101, 102)")
    cursor.execute("DELETE FROM MEMBER WHERE MemberID IN (1, 2)")
    cursor.execute("DELETE FROM CLASS WHERE ClassID IN (1, 2)")
    cursor.execute("DELETE FROM PERSONAL_TRAINING_SESSION WHERE SessionID IN (1, 2)")
    cursor.execute("DELETE FROM Class_Attendance WHERE ClassID IN (1, 2)")
    conn.commit()
    print("Dummy data deleted successfully.")

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    action = input("Insert or Delete dummy data (i/d): ")
    if action == "i":
        print("Inserting dummy data")
        insert_dummy_data()
    elif action == "d":
        print("Deleting dummy data")
        delete_dummy_data()
    else:
        print("invalid input")