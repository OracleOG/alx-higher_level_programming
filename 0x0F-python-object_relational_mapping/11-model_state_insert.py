#!/usr/bin/python3
"""Script to add a State object to the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

    new_record = State(name='Louisiana')
    session.add(new_record)

    session.commit()
    print(new_record.id)
