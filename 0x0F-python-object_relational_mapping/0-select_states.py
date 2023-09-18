#!/usr/bin/python3

"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

mydb = MySQLdb.connect(
    host="localhost",
    user=username,
    passwd=password,
    db=database
)

mycursor = mydb.cursor()

sql = f"SELECT * FROM states ORDER BY states.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for state in myresult:
    print(state)

mycursor.close()
mydb.close()
