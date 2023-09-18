#!/usr/bin/python3

import MySQLdb
import sys


def main():
    """Lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa"""
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

    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for state in myresult:
        print(state)

    mycursor.close()
    mydb.close()


if __name__ == '__main__':
    main()
