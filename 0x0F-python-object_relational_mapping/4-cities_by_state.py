#!/usr/bin/python3
"""Module that retrieves and prints all\
        states from a MySQL database using SQLAlchemy."""

import MySQLdb
import sys


def list_citis(username, password, database):
    """
    lists all cities from the database hbtn_0e_4_usa
    Args:
        username = mysql username
        password = mysql password
        database = mysql database
    """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database,
        host='localhost',
        port=3306
    )
    mycursor = db.cursor()

    sql_query = ("SELECT
                 cities.id, cities.name, states.name
                 FROM cities
                 JOIN states
                 ON cities.state_id=states.id
                 ORDER BY cities.id ASC")
    mycursor.execute(sql_query)
    allCities = mycursor.fetchall()

    for city in allCities:
        print(city)

    db.close()

    if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_citis(username, password, database)
