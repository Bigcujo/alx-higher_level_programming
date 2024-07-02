#!/usr/bin/python3
""" 
prints all the city object with and the states connected to it
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    for instances in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instances[0] + ": (" + str(instances[1]) + ") " + instances[2])
