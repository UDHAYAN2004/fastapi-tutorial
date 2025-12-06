from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base # to create models
from sqlalchemy.orm import sessionmaker # for creating a session for communication with database

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:udhayan@localhost:5432/blogdb"

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(bind=engine ,autocommit=False,autoflush=False)
#autocommit==True means changes are saved automatically.
#autocommit==False means changes are not saved automatically until we call .commit()

#autoFlush==True means changes are flushed automatically.
#autoFlush==False means changes are not flushed automatically until we call .flush()
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()