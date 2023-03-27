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
    statement = select(database_setup.Story).order_by(database_setup.Story.date.desc())
    results = session.exec(statement)
    heroes = results.all()
    print(type(heroes[0]))
    return heroes

def add_story(session, genre, prompt, heading):
    story = database_setup.Story(genre=genre, prompt=prompt, heading=heading)
    session.add(story)
    session.commit()

def get_stories(session, genre):
    statement = select(database_setup.Story).where(database_setup.Story.genre == genre).order_by(database_setup.Story.date.desc())
    results = session.exec(statement)
    story = results.all()
    return story