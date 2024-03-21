import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mydb = mysql.connector.connect(
  host=os.getenv('DB-HOST'),
  user=os.getenv('DB-USERNAME'),
  password=os.getenv('DB-PASSWORD'),
  database=os.getenv('DB-DATABASE')
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM jym.member")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)