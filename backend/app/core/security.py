from datetime import datetime,timedelta
from passlib.context import CryptContext
from jose import jwt


from backend.app.core.config import settings


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_pass(plain:str,hassed:str)->bool:
    return pwd_context.verify(plain,hassed)

def create_access_token(data:dict,expires_delta:timedelta):
    to_encode=data.copy()
    to_encode["exp"]=datetime.utcnow()+expires_delta
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def decode_token(token:str)->dict:
    return jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )

