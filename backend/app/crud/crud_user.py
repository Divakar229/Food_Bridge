from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.model import User
from ..schemas.schema import UserCreate as UserSchema

## josn(in frontend)-->pydantic model(by fastapi)--->dict-->sqlalchemy model
def createUser(db:Session,user:UserSchema,admin):
    existing_user = db.query(User).filter(User.admin_id == admin.id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists for this admin")
    data=User(**user.dict(exclude={"admin_id"}),admin_id=admin.id)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data



def getRole(db:Session,role:str):
    return db.query(User).filter(User.role==role).all()

