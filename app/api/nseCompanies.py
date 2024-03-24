from fastapi import APIRouter, Depends, Query
from app.utils.apiResponse import apiResponse
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.nseCompanyModel import NSEcompany


# base endpoint: /api/nse-companies
router = APIRouter()


@router.get("/", tags=["nse-companies"])
async def get_nse_companies(
        pageNumber: int = Query(1, description="Page Number"),
        limit: int = Query(20, description="Limit the number of items"),
        db: Session = Depends(get_db)
) -> JSONResponse:
    if limit>100:
        return apiResponse(
            statusCode=400,
            message="Limit exceeded! Can't fetch more than 100."
        )
    skipFrom = pageNumber - 1
    responseData = db.query(NSEcompany).offset(skipFrom).limit(limit).all()
    responseData = NSEcompany.list_to_json(responseData)
    return apiResponse(
        responseData
    )


