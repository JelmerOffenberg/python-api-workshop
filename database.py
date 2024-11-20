from sqlmodel import create_engine, SQLModel

# Any tables that you would define, should be defined below this line using SQLModel.


# This is the database engine that will be used to connect to the database.
connect_args = {"check_same_thread": False}
engine = create_engine("sqlite:///sqlite.db", echo=True, connect_args=connect_args)


# This will create the tables in the database. Optionally, you can drop all tables before creating them.
# SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    # Use this section to perform any testing of the database.py file.
    print("Hello, World!")