import database_setup
from sqlmodel import Field, Session, SQLModel, create_engine, select

def getSession():
    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
    session = Session(engine)
    return session

def print_database(session):
    statement = select(database_setup.Story)
    results = session.exec(statement)
    heroes = results.all()
    print(heroes)

def add_story(session, genre, prompt, heading):
    story = database_setup.Story(genre=genre, prompt=prompt, heading=heading)
    session.add(story)
    session.commit()