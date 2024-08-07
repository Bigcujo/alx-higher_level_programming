#!/usr/bin/python3

"""
Contains State class and Base, an instance of declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

myMetaData = MetaData()
Base = declarative_base(metadata=myMetaData)


class State(Base):
    """
    state class with id, name and table name of the class
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
