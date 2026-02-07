from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
import logging

from backend.app.api.database import db_dependency
from backend.app.schemas.schema import User as UserSchema
from backend.app.curd import crud_user 
from typing import Annotated

db_depends=Annotated[Session,Depends(db_dependency)]

logger=logging.getLogger(__name__)

router=APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def createUser(user:UserSchema,db:db_depends):
    logger.info("creating new user")

    return crud_user.createUser(db,user)


@router.get("/role/{role}")
def get_user_by_role(role: str, db: Session = Depends(db_dependency)):
    logger.info(f"Fetching user with role={role}")

    user = crud_user.getRole(db, role)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user
