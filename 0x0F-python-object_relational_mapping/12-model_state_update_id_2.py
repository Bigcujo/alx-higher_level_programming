#!/usr/bin/python3
""" this script will edit the instance with id = 2, and change the object name to = Mexico
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
    session = Sessions()
    new_instances = session.query(State).filter_by(id=2).first()
    new_instances.name = 'New Mexico'
    session.commit()
