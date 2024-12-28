#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":

    print('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

     # Construct connection string
    connection_string = f'mysql+mysqldb://{username}:{password}@localhost/{database}'

    # Create engine
    engine = create_engine(connection_string, pool_pre_ping=True)

    Base.metadata.create_all(engine)