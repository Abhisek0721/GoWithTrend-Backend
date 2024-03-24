from fastapi import APIRouter
from app.api import users, auth, nseCompanies

api_router = APIRouter()

api_router.include_router(users.router, prefix="/user", tags=["user"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(nseCompanies.router, prefix="/nse-companies", tags=["nse-companies"])
