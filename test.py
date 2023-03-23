# story_1 = Story(genre="Fantasy", prompt="A hero is born", heading="The Beginning")
# session = Session(engine)

# session.add(story_1)

# session.commit()


    
# session.close()

import repo

session = repo.getSession()
repo.print_database(session)