#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(
        (State.id == City.state_id)).order_by(State.id, City.id).all()
    
    curr_state = None
        
    for state, city in results:
        if state != curr_state:
            curr_state = state
            print("{}: {}".format(state.id, state.name))
        print("\t{}: {}".format(city.id, city.name))

    session.commit()

    session.close()
