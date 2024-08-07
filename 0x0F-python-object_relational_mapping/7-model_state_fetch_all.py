#!/usr/bin/python3
"""
creats a link to the database and extracts the data in the table.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
            engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2],  sys.argv[3]))
            Base.metadata.create_all(engine)
            Sessions = sessionmaker(bind=engine)
            session = Sessions()
            for objects in session.query(State).order_by(State.id):
                print(objects.id, objects.name, sep=": ")


