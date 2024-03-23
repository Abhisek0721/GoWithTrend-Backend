from fastapi.responses import JSONResponse

def apiResponse(data=None, statusCode:int=200, message:str="", errors:any=None ):
    if data and data.get('_sa_instance_state'):
        del data['_sa_instance_state']
    return JSONResponse(
        status_code=statusCode,
        content={
            "data": data,
            "message": message,
            "errors": errors
        }
    )