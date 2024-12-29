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

    username, password, database, = sys.argv[1:]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}'
                           f'@localhost:3306/{database}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state_id=new_state.id)
    new_state.cities.append(new_city)
    session.add(new_state, new_city)

    session.commit()
    print("id  name")
    print(new_state.id, new_state.name)
    print('id  name  state_id')
    print(new_city.id, new_city.name, new_city.state_id)
