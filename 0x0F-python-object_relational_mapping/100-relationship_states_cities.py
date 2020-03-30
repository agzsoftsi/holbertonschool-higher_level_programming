#!/usr/bin/python3
"""
Task 100
Write a script that creates the State "California" with the
City "San Francisco" from the database hbtn_0e_100_usa
"""

if __name__ == "__main__":
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    sf = City(name='San Francisco')
    california = State(name='California')
    california.cities.append(sf)
    session.add(sf)
    session.add(california)
    session.commit()
    session.close()
