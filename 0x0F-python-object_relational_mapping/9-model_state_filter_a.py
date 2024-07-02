#!/usr/bin/python3
"""
prints the object in the table that has "a" in it.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    for instances in session.query(State).filter(State.name.like('%a%')):
        print(instances.id, instances.name, sep=": ")

