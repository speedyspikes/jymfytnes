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
#I'll fix this formatting later...
sql = """INSERT INTO jym.member 
                 (MemberEmail, 
                 MembershipTier, 
                 MemberPhone, 
                 MemberName, 
                 MemberID, 
                 MemberGender)
                 VALUES
                 (%s, %s, %s, %s, %s, %s)"""
val = ("john@example.com", "1", "4801234567", "John Smith", 123, 1)
mycursor.execute(sql, val)

mydb.commit()

myresult = mycursor.fetchall()

for x in myresult:
  print(x)