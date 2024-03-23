# db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.constants import constants
from .base import Base

# Database URL
# DATABASE_URL = f"mysql+mysqlconnector://{constants.DB_USERNAME}:{constants.DB_PASSWORD}@localhost:3306/{constants.DATABASE_NAME}"
DATABASE_URL = constants.DB_DOMAIN
print(f"DATABASE_URL: {DATABASE_URL}")

# Create a database engine
engine = create_engine(
    DATABASE_URL, 
    # echo=True,
    # client_encoding='utf8',
    # connect_args={"sslmode": "disable"}
)

# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for other modules
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
