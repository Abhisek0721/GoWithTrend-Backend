from fastapi import FastAPI, HTTPException
from app.api import api_router
from app.middlewares.error_handler import http_error_handler, unhandled_exception_handler
from app.middlewares import rate_limiter, verify_token
import threading
from app.jobs import startJobs
from app.constants import constants


app = FastAPI()

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=startJobs)
scheduler_thread.start()

# Add middleware for authentication
# app.add_middleware(auth.AuthenticationMiddleware)
app.add_middleware(rate_limiter.RateLimitingMiddleware)

# Add middleware for error handling
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=constants.PORT)
