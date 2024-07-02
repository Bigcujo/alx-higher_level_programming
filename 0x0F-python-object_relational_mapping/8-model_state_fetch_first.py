#!/usr/bin/python3
"""
this prints the first state object in the database hbtn_0e_6_usa
"""
import sys 
import model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    instances = session.query(State).first()
    if (instances == None):
        print("Nothing")
    else:
        print(instances.id, instance.name, sep=": ")
