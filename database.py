import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def create_client():
  mydb = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE')
  )
  return mydb


# If you run the database.py file, it will test your connection.
if __name__ == "__main__":
    client = create_client()
    # Try to show member data
    try:
      mycursor = client.cursor()
      mycursor.execute("SELECT * FROM jym.member")
      myresult = mycursor.fetchall()
      for x in myresult:
        print(x)
    except Exception as e:
        print(e)