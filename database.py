from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """This is the base class for all models in the application.

    This is a pattern specific to SQLAlchemy and directly taken from the official documentation.
    You must use this class as a base class for all your data models.
    """
    pass

# Any tables that you would define, should be defined below this line.


# This is the database engine that will be used to connect to the database.
engine = create_engine("sqlite:///sqlite.db", echo=True)


# This will create the tables in the database. Optionally, you can drop all tables before creating them.
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


if __name__ == '__main__':
    # This is a simple test to check if the database is working.
    print("Hello, World!")