from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.utils.apiResponse import apiResponse
from app.schemas.signupSchema import SignupSchema
from app.schemas.loginSchema import LoginSchema
from app.schemas.tokenSchema import TokenSchema
from app.models.userModel import User
from app.db.session import get_db
from sqlalchemy.orm import Session

# base endpoint: /api/auth
router = APIRouter()


@router.post("/login", tags=["auth"], response_model=TokenSchema)
async def login(loginPayload: LoginSchema, db: Session = Depends(get_db)) -> JSONResponse:
    check_user = db.query(User).filter(
        User.email == loginPayload.email).first()
    # verify email and password
    if not check_user or not check_user.verify_password(loginPayload.password):
        return apiResponse(
            statusCode=401,
            message="Invalid email or password"
        )

    response_data = check_user.generateAccessToken()
    return apiResponse(data=response_data, message="Loggedin successfully!")


@router.post("/signup", tags=["auth"])
async def signup(signupPayload: SignupSchema, db: Session = Depends(get_db)) -> JSONResponse:
    print(signupPayload.__dict__)
    check_user = db.query(User).filter(
        User.email == signupPayload.email).first()
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
