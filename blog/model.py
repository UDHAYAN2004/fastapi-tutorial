from .database  import Base
from sqlalchemy import Column, Integer, String, Boolean

#creating models which is to be in database
class Blog(Base):
    __tablename__="blogs"

    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    description=Column(String)
    published=Column(Boolean, default=True)

#creating user
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
