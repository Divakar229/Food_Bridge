from sqlalchemy.orm import Session
from ..models.admin import Admin


def get_admin_by_email(db:Session,email:str):
    return db.query(Admin).filter(Admin.email==email).first()

def get_admin_by_id(db:Session,id:int):
    return db.query(Admin).filter(Admin.id==id).first()

def create_admin(db:Session,email:str,hass_pass:str):
    data=Admin(email=email,password=hass_pass)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data