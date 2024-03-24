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
from app.schemas.changePasswordSchema import ChangePasswordSchema

# base endpoint: /api/user
router = APIRouter()


@router.get("/", tags=["user"], response_model=GetUserSchema)
async def get_user(current_user: dict = Depends(verify_token), db: Session = Depends(get_db)) -> JSONResponse:
    userId = current_user.get("userId")
    responseData = db.query(User).filter(
        User.id == userId).options(defer(User.password)).first()
    return apiResponse(
        responseData.to_json()
    )


@router.patch("/", tags=["user"])
async def update_user(userPayload: UpdateUserSchema, current_user: dict = Depends(verify_token), db: Session = Depends(get_db)) -> JSONResponse:
    userId = current_user.get("userId")
    user = db.query(User).filter(User.id == userId).first()
    user.firstName = userPayload.firstName
    user.lastName = userPayload.lastName
    responseData = user.to_json()
    db.commit()
    return apiResponse(
        data=responseData,
        message="User updated successfully"
    )

@router.patch("/change-password", tags=["user"])
async def update_user(passwordPayload: ChangePasswordSchema, current_user: dict = Depends(verify_token), db: Session = Depends(get_db)) -> JSONResponse:
    userId = current_user.get("userId")
    user = db.query(User).filter(User.id == userId).first()
    if not user.verify_password(passwordPayload.currentPassword):
        return apiResponse(
            statusCode=401,
            message="Invalid current password!"
        )
    user.set_password(passwordPayload.newPassword)
    db.commit()
    return apiResponse(
        message="Password updated successfully"
    )