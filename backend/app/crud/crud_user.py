from sqlalchemy.orm import Session
from ..models.model import User
from ..schemas.schema import UserCreate as UserSchema

## josn(in frontend)-->pydantic model(by fastapi)--->dict-->sqlalchemy model
def createUser(db:Session,user:UserSchema,):
    data=User(**user.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def getRole(db:Session,role:str):
    return db.query(User).filter(User.role==role).all()

