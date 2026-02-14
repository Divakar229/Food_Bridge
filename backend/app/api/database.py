from sqlalchemy import create_engine # to create engine for the database connectivity
from sqlalchemy.orm import sessionmaker# to create to session to talk with database(factory that creats session class)
import os
from dotenv import load_dotenv

load_dotenv()



base_url=os.getenv("DATABASE_URL")
engine=create_engine(base_url)


SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) # calling this it creates real database session (objects)

def db_dependency():
    db=SessionLocal()
    try:
        yield db   #yield pause the function (waits and give a session or the api route)
    finally:
        db.close()