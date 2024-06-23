#!/usr/bin/python3
"""
Connects to MySQL DB and fetch all states from 'states' table,
sorted by ID, and print them.
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

    query = "SELECT * FROM states ORDER BY id;"

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
