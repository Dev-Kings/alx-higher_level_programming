#!/usr/bin/python3
"""
Script that creates the State "California" with City "San Francisco"
from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Create the State "California" with the City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add the new state and city to the session
    session.add(new_state)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
