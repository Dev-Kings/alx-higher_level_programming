#!/usr/bin/python3
"""
Connects to MySQL DB and fetch all cities from 'cities' table,
where state name is passed as argument, sorted by ID, and print them.

Usage:
    python 5-filter_cities.py <mysql_username> <mysql_password>
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
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id;
    """

    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    cursor.close()
    conn.close()
