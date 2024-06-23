#!/usr/bin/python3
"""
Deletes all State objects that contain the letter 'a' in their name
from the database hbtn_0e_6_usa
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

    # Query all State objects containing letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete matched states
    for state in states_with_a:
        session.delete(state)

    # Commit the transaction to the database
    session.commit()

    # Close the session
    session.close()
