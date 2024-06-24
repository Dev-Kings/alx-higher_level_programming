#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(uname, pwd, db))

    # Bind Base class to the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query City objects, sorted by id, with state name included
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close the session
    session.close()
