#!/usr/bin/python3
"""
    prints the first instance oaf an argumnets passed to the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Sessions =  sessionmaker(bind=engine)
    sessions = Sessions()
    instances = sessions.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instances[0].id)
    except IndexError:
        print("Not found")


