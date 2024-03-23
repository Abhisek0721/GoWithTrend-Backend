from fastapi import APIRouter
from fastapi import Depends
from app.utils.apiResponse import apiResponse
from app.middlewares.verify_token import verify_token
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, defer
from app.db.session import get_db
from app.models.userModel import User
from app.schemas.getUserSchema import GetUserSchema
from app.schemas.updateUserSchema import UpdateUserSchema

# base endpoint: /api/user
router = APIRouter()


@router.get("/", tags=["user"], response_model=GetUserSchema)
async def get_user(current_user: dict = Depends(verify_token), db: Session = Depends(get_db)) -> JSONResponse:
    userId = current_user.get("userId")
    responseData = db.query(User).filter(
        User.id == userId).options(defer(User.password)).first()
    return apiResponse(
        responseData.__dict__
    )


@router.patch("/", tags=["user"])
async def update_user(userPayload: UpdateUserSchema, current_user: dict = Depends(verify_token), db: Session = Depends(get_db)) -> JSONResponse:
    userId = current_user.get("userId")
    user = db.query(User).filter(User.id == userId).first()
    user.firstName = userPayload.firstName
    user.lastName = userPayload.lastName
    responseData = {
        "userId": user.id,
        "firstName": user.firstName,
        "lastName": user.lastName,
        "email": user.email
    }
    db.commit()
    return apiResponse(
        data=responseData,
        message="User updated successfully"
    )
