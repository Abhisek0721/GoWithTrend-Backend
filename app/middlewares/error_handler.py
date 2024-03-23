from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.utils.apiResponse import apiResponse

async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return apiResponse(
        None,
        exc.status_code,
        exc.detail,
        exc.args
    )

async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return apiResponse(
        None,
        500,
        "Internal server error!",
        exc.args
    )
