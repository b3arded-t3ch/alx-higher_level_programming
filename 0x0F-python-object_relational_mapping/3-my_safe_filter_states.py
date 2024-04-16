#!/usr/bin/python3

import MySQLdb
import sys


def list_statesS(username, password, database, state_name):
    """
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument, with injection proof.
    Args:
        username = mysql username
        password = mysql password
        database = mysql database
        name = name to be matched
    """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database,
        host='localhost',
        port=3306
    )
    mycursor = db.cursor()

    sqlquery = ("SELECT * FROM states WHERE name = %s ORDER BY id ASC")
    mycursor.execute(sqlquery, (state_name,))
    allStates = mycursor.fetchall()

    for state in allStates:
        if state[1] == name:
            print(state)

    db.close()

    if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        name = sys.argv[4]

        list_statesS(username, password, database, name)
