from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database import Blogs, Base

engine = create_engine('sqlite:///blogs.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Insert a Blog in the blogs table
new_blog = Blogs(name='Leslie', blog='My Blog', date=datetime.datetime.now())
session.add(new_blog)
session.commit()
