#!/usr/bin/python3
"""Script to print the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, database):
    """Function to print the first State object from the database"""
    # Create engine to connect to the database
    engine = create_engine(f'''mysql+mysqldb://{username}:{password}
                           @localhost:3306/{database}''')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the first State object if it exists
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("No State objects found in the database.")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    print_first_state(username, password, database)
