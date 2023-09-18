#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    state_to_search = sys.argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_to_search).first()

    if not state:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()
