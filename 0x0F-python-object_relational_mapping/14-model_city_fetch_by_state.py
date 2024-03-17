#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # Create a MySQL engine and session
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all City objects from the database and print them
    cities = session.query(State, City).join(City).order_by(City.id)
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
