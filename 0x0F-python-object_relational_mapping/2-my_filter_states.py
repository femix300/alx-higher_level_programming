#!/usr/bin/python3

import MySQLdb
import sys


def main():
    """Takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument."""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id".format(name)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for state in myresult:
        print(state)

    mycursor.close()
    mydb.close()

if __name__ == '__main__':
    main()