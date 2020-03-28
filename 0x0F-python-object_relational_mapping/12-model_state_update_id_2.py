#!/usr/bin/python3
"""
Task 12
Change the name of the State where id = 2 to New Mexico
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
    two = session.query(State).filter_by(id=2).first()
    two.name = 'New Mexico'
    session.commit()
    session.close()
