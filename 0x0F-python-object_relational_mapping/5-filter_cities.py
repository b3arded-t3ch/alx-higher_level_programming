#!/usr/bin/python3

import MySQLdb
import sys


def list_citis_by_states(username, password, database, state_name):
    """
    takes in the name of a state as an argument and lists all cities
    of that state, using the database hbtn_0e_4_usa.
    Args:
        username = mysql username
        password = mysql password
        database = mysql database
        state_name = state searched
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
                 ORDER BY cities.id ASC"
                 )
    mycursor.execute(sql_query, (state_name,))
    all_cities_n_states = mycursor.fetchall()
    for citi_n_state in all_cities_n_states:
        if citi_n_state[2] == state_name:
            print(citi_n_state[1])

    db.close()

    if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        list_citis_by_states(username, password, database, state_name)
