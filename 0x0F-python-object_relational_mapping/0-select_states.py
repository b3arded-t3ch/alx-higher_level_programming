#!/usr/bin/python3
"""Module that lists all states from mySQL database"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Lists all states from the database hbtn_0e_0_usa.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database

    Returns:
        None
    """

# connect to the database and get cursor object
db = MySQLdb.connect(
    user=username,
    passwd=password,
    db=database,
    host="localhost",
    port=3306
)
mycursor = db.cursor()

# cursor object executes sql query, fetches the result, and prints it
mycursor.execute("SELECT * FROM states ORDER BY id ASC")
myresult = mycursor.fetchall()

for result in myresult:
    print(result)

# connector object closes connection to the database
db.close()

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    states = list_states(username, password, database)
