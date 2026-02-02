from slowapi import Limiter,_rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse


limiter=Limiter(key_func=get_remote_address)

def init_limiter(app:FastAPI):
    app.state.limiter=limiter


    @app.exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)
    async def rate_limit_handler(request:Request,exc:RateLimitExceeded):
        return JSONResponse(
            status_code=429,
            content={"message":"too many request,slow down!"}
        )
