from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from app.db.base import Base
from app.db.session import engine
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from app.constants import constants

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
        self.password = hashed_password.decode('utf-8')
    
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def generateAccessToken(self):
        payload = {
            "userId": self.id,
            "email": self.email,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=constants.TOKEN_EXPIRATION)
        }
        # generating access_token
        access_token = jwt.encode(payload, constants.JWT_SECRET_KEY, algorithm="HS256")
        # generating refresh_token
        payload.pop("exp")
        refresh_token = jwt.encode(payload, constants.JWT_SECRET_KEY, algorithm="HS256")
        response_data = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
        return response_data
    
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "verified": self.verified,
        }
    
    @classmethod
    def list_to_json(cls, data):
        return [each.to_json() for each in data]

# Create the tables
Base.metadata.create_all(bind=engine)
