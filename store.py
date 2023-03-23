from typing import Optional
from datetime import datetime

# One line of FastAPI imports here later 👈
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Story(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    genre: str = Field(index=True)
    prompt: str
    heading: str
    date: datetime = Field(default_factory=datetime.now)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


#SQLModel.metadata.create_all(engine)



story_1 = Story(genre="Fantasy", prompt="A hero is born", heading="The Beginning")
session = Session(engine)

session.add(story_1)

session.commit()

with Session(engine) as session:
    statement = select(Story)
    results = session.exec(statement)
    heroes = results.all()
    print(heroes)
    
session.close()
