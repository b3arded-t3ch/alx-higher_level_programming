#!/usr/bin/python3

import MySQLdb
import sys


def list_statesF(username, password, database, name):
    """
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
    Args:
        useranme = mysql username
        password = mysql password
        database = mysql database
        name = state name searched
    """

    db = MySQLdb.connect(
        username=username,
        passwd=password,
        db=database,
        host='localhost',
        port=3306
    )
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = mycursor.fetchall()

    for state in states:
        if state[1] == name:
            print(state)

    if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        name = sys.argv[4]

        list_statesF(username, password, database, name)
