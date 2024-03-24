from fastapi.responses import JSONResponse

def apiResponse(data=None, statusCode:int=200, message:str="", errors:any=None ):
    return JSONResponse(
        status_code=statusCode,
        content={
            "data": data,
            "message": message,
            "errors": errors
        }
    )