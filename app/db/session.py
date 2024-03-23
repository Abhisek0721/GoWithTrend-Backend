# db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base

# Database URL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/gowithtrend"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for other modules
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
