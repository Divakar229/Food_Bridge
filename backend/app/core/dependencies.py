from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session


from backend.app.api.database import db_dependency
from backend.app.core.security import decode_token
from ..curd.curd_admin import get_admin_by_id

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/admin/token')


def get_current_admin(token:str=Depends(oauth2_scheme),
                      db:Session=Depends(db_dependency)):
    try:
        playload=decode_token(token)
        admin_id=playload.get("id")

        if admin_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid token"
            )
        admin=get_admin_by_id(db,admin_id)

        if not admin:
             raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="admin not found"
            )
        return admin
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="could not validate token"
        )