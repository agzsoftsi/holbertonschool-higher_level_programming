#!/usr/bin/python3
"""
Task 13
Write a script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
