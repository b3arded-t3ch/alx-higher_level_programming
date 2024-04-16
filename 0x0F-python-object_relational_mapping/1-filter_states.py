#!/usr/bin/python3

import MySQLdb
import sys


def list_statesN(username, password, database):
    """
     lists all states with a name starting with N (upper N)
     from the database hbtn_0e_0_usa.
     Args:
        username = mysql username
        password = mysql password
        database = mysql database
    """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database,
        host="localhost",
        port=3306
    )

    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = mycursor.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)

    db.close()

    if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_statesN(username, password, database)
