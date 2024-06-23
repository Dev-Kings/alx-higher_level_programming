#!/usr/bin/python3
"""
Connects to MySQL DB and fetch all cities from 'cities' table,
sorted by ID, and print them.

Usage:
    python 4-cities_by_state.py <mysql_username> <mysql_password>
    <database_name>
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

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id;
    """

    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    conn.close()
