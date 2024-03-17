#!/usr/bin/python3
"""Defines the City class."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Represents a city for a MySQL database."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __str__(self):
        """Returns the string representation of a City instance."""
        return "{}: ({}) {}".format(self.state.name, self.id, self.name)
