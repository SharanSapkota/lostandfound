import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://lostandfound_9bfj_user:lP4P7g9Q4jcXjcq0kbR9PjL8dTEHDG3j@dpg-d7erugosfn5c738hkd4g-a.oregon-postgres.render.com/lostandfound_9bfj"
print("Loaded DB URL:", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()