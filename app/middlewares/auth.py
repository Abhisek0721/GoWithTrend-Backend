from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class AuthenticationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    def __verify_token(self, token):
        return True

    async def dispatch(self, request: Request, call_next):
        # Your authentication logic here
        token = request.headers.get("Authorization")
        if not token or not self.__verify_token(token):
            raise HTTPException(status_code=401, detail="Invalid token")
        
        response = await call_next(request)
        return response
