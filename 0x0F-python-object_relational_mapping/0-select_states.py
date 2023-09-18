#!/usr/bin/python3

import MySQLdb
import sys


def main():
    """Lists all states from the database hbtn_0e_0_usa"""

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


if __name__ == '__main__':
    main()
