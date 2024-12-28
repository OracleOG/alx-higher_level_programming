#!/usr/bin/python3
"""Script to list all City objects from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State


def list_cities(username, password, database):
    """Function to list all city objects from the database"""
    # Create engine to connect to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}'
                           f'@localhost:3306/{database}', pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all city objects and sort by cities.id in ascending order
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for instance in (
            session.query(
                State.name, City.id, City.name
                ).filter(State.id == City.state_id)):
        print(instance[0] + ': (' + str(instance[1]) + ') ' + instance[2])

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
