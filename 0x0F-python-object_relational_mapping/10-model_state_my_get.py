#!/usr/bin/python3
"""
Prints State objects with the name passed as argument, from the database
hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine and conenct to MySQL server
    engine = create_engine(
            f'mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}',
            pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
