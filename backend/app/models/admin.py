from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from datetime import datetime

from backend.app.models.model import Base

class Admin(Base):
    __tablename__="admins"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True,nullable=False)
    password=Column(String,nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)

    create_at=Column(DateTime,default=datetime.utcnow)