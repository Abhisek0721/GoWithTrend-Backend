from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from app.constants import constants
from app.models.userModel import User
from sqlalchemy.orm import Session
from app.db.session import get_db


# Dependency for verifying JWT token
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()), db: Session = Depends(get_db)) -> dict:
    try:
        payload = jwt.decode(
            credentials.credentials,
            constants.JWT_SECRET_KEY,
            algorithms="HS256"
        )
        userId = payload.get("userId")
        user = db.query(User).filter(User.id == userId).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
