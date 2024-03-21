import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def create_client():
  mydb = mysql.connector.connect(
    host=os.getenv('DB-HOST'),
    user=os.getenv('DB-USERNAME'),
    password=os.getenv('DB-PASSWORD'),
    database=os.getenv('DB-DATABASE')
  )
  return mydb


# If you run the dtabase.py file, it will test your connection.
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