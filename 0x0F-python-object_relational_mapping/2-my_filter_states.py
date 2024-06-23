#!/usr/bin/python3
"""
Connects to MySQL DB and fetch all states from 'states' table,
where name matches argument passed, sorted by ID, and prints them.

Usage:
    python 2-my_filter_states.py <mysql_username> <mysql_password>
        <database_name> 'argument'
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306
        )

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER\
            BY id;".format(sys.argv[4])

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
