#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database
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

    engine = create_engine(
            f'mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}',
            pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects containing letter 'a', order by id
    states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
