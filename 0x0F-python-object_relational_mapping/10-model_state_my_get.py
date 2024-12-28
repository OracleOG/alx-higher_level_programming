#!/usr/bin/python3
"""Script to print the first State object from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("""Usage: {} <username> <password>
               <database> <name>""".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, search_name = sys.argv[1:]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}'
                           f'@localhost:3306/{database}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # deal with SQL injections
    name = '%s' % search_name

    for states in session.query(State).filter(State.name.like(f'%{name}%')):
        if states:
            print(f"{states.id}")
        else:
            print("Not found")
'''
    # Construct the query with a bound parameter
    query = session.query(State).filter(State.name.like(':name'))

    # Execute the query with the search term as a bound parameter
    states = session.execute(query, {'name': f'%{search_name}%'})

    # Print the results
    for state in states:
    print(f"{state.id}: {state.name}")



    #session.close()
'''
