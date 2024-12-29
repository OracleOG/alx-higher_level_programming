#!/usr/bin/python3
"""Script to add a State object to the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""Usage: {} <username> <password> <database> <
              name>""".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}'
                           f'@localhost:3306/{database}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)

    session.commit()
