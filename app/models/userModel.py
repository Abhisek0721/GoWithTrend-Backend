from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from app.db.base import Base
from app.db.session import engine
import bcrypt

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=False)
    email  = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    verified = Column(Boolean, default=False)

    # __table_args__ = (
    #     CheckConstraint('email ~* \'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}\'', name='valid_email'),
    #     CheckConstraint('password ~* \'(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}\'', name='valid_password'),
    # )

    def __init__(self, firstName, lastName, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_password
    
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Create the tables
Base.metadata.create_all(bind=engine)