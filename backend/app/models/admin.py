from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, relationship

from backend.app.models.model import Base

class Admin(Base):
    __tablename__="admins"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True,nullable=False)
    password=Column(String,nullable=False)

    create_at=Column(DateTime,default=datetime.utcnow)

    user: Mapped["User"] = relationship(
        "User", uselist=False, back_populates="admin"
    )