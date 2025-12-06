from .database  import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship


#creating user
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    blogs=relationship('Blog',back_populates='createdBy')


#creating models which is to be in database
class Blog(Base):
    __tablename__="blogs"

    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)
    title=Column(String,nullable=False)
    description=Column(String,nullable=False)
    published=Column(Boolean, default=True)
    createdBy=relationship('User',back_populates='blogs')

