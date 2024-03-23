from fastapi import APIRouter, Depends
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.utils.apiResponse import apiResponse
from app.schemas.signupSchema import SignupSchema
from app.models.userModel import User
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# base endpoint: /api/auth


@router.post("/login", tags=["auth"])
async def login():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.post("/signup", tags=["auth"])
async def signup(signupPayload: SignupSchema, db: Session = Depends(get_db)) -> JSONResponse:
    print(signupPayload.__dict__)
    check_user = db.query(User).filter(User.email == signupPayload.email).first()
    if check_user:
        return apiResponse(
            statusCode=400,
            message="User with this email already exist!"
        )
    user = User(
        firstName=signupPayload.firstName, 
        lastName=signupPayload.lastName, 
        email=signupPayload.email, 
        password=signupPayload.password
    )
    db.add(user)
    db.commit()
    return apiResponse(
        message="Successfully created an account!"
    )
