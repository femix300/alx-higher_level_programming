#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    mycursor = mydb.cursor()

    sql = sql = ("SELECT c.* FROM cities c "
                 "INNER JOIN states s ON c.state_id = s.id "
                 "WHERE s.name LIKE BINARY %s")

    mycursor.execute(sql, (state_name,))
    cities = mycursor.fetchall()

    city_names = [city[2] for city in cities]

    result = ', '.join(city_names)

    print(result)

    mycursor.close()
    mydb.close()
