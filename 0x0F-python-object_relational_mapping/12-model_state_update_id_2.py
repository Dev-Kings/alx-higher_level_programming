#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
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

    # Query for state with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State object
    state_to_update.name = 'New Mexico'

    # Commit the transaction to the database
    session.commit()

    # Close the session
    session.close()
