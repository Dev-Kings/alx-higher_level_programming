#!/usr/bin/python3
"""
Module contains the class definition of a City class and an instance
Base = declarative_base(). The City class definition is mapped to the cities
table in MySQL database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that links to the MySQL table 'cities'.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
