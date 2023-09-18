#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
and their corresponding states
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    mycursor = mydb.cursor()

    sql = ("SELECT cities.id, cities.name, states.name "
           "FROM cities "
           "JOIN states ON cities.state_id = states.id "
           "ORDER BY cities.id")

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for state in myresult:
        print(state)

    mycursor.close()
    mydb.close()
