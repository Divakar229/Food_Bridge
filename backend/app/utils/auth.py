from fastapi import Depends,APIRouter,HTTPException,status
from typing import Annotated #Annotated = type + extra information
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt,JWTError
from passlib.context import CryptContext
from schema import Users
from backend.app.models.model import userS
from sqlalchemy.orm import Session
from backend.app.api.database import db_dependency
from datetime import datetime,timedelta

SECRET_KEY = "9a5c3d0f7b8a9c4e51f21f4ab7d2e1e6481a9f2c12c35dfe7b2e1dffb6c5a8c3"
# used for password hasing and encription jwt login(using token)
ALGORITHM = "HS256"

OAuth2_bearer=OAuth2PasswordBearer(tokenUrl='/admin/token')
bcrypt_context=CryptContext(schemes=['bcrypt'],deprecate="auto")
db_depend=Annotated[Session,Depends(db_dependency)]  # db_depend:session=Depends(db_dependency)

router=APIRouter(
    prefix=['/admin'],
    tags="/login"
)

@router('/')
def craete_user(us:Users,db:db_depend):
    exists=db.query(userS).filter(us.email==userS.email).first()
    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user already exists"
        )
    data=userS(    # data={**us.dict()}
        email=us.email,
        password=bcrypt_context(us.password)
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
 

def authenticate(email:str,password:str,db:db_depend):
    valid=db.query(userS).filter(email== userS.email).first()
    if not valid:
        return False
    if not bcrypt_context.verify(userS.password,password):
        return False
    return valid
    
def create_access_token(id:int,email:str,expiry:timedelta):
    expires=datetime.utcnow()+expiry
    encode={"id":id,"sub":email,"exp":expires}
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

def get_current_user(token:Annotated[str,Depends(OAuth2_bearer)]):
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    email:str=payload.get("sub")
    id:str=payload.get("id")
    try:
     if not id or email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="invalid username and password" 
                                )
     return {"username":email,"user_id":id}
    except:
         HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="invalid username and password" 
         )
#Depends()  automatically creates required objects like DB sessions or tokens and injects them into the route function.
#Depends() injects the dependency’s RETURN VALUE into the route function. --->main
@router.post("/token")
async def login_access_token(db:db_depend,form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    user=authenticate(form_data.email,form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="user not found"
        )
    token=create_access_token(user.id,user.email,timedelta(30))
    return {"token":token,"token_type":"bearer"}
