import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Blogs(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    blog = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)


engine = create_engine('sqlite:///blogs.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
