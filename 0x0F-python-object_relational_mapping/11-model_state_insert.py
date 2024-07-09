#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Sessions = sessionmaker(bind=engine)
    Session = Sessions()
    new_state = State(name='Louisiana')
    Session.add(new_state)
    new_Instances = Session.query(State).filter_by(name='Louisiana').first()
    print(new_Instances.id)
    Session.commit()