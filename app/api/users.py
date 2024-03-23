from fastapi import APIRouter
from fastapi import Depends
from app.utils.apiResponse import apiResponse
from app.middlewares.verify_token import verify_token
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, defer
from app.db.session import get_db
from app.models.userModel import User
from app.schemas.getUserSchema import GetUserSchema

# base endpoint: /api/user
router = APIRouter()


@router.get("/", tags=["user"], response_model=GetUserSchema)
async def get_user(current_user: dict = Depends(verify_token), db: Session = Depends(get_db)) -> JSONResponse:
    userId = current_user.get("userId")
    responseData = db.query(User).filter(User.id == userId).options(defer(User.password)).first()
    return apiResponse(
        responseData.__dict__
    )


@router.get("/{user_id}", tags=["user"])
async def read_user(user_id: int):
    return {"user_id": user_id, "username": "Foo"}
