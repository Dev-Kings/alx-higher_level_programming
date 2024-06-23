#!/usr/bin/python3
"""
Script that adds State object to the database hbtn_0e_6_usa
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

    # Create a new State object
    new_state = State(name='Louisiana')

    # Add new State object to the session
    session.add(new_state)

    # Commit the transaction to the database
    session.commit()

    # Print the state's id after creation
    print(new_state.id)

    # Close the session
    session.close()
