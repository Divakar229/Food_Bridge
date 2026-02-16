from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean,ForeignKey
from sqlalchemy.orm import declarative_base,Mapped,mapped_column,relationship
from datetime import datetime


Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    admin_id: Mapped[int] = mapped_column(Integer, ForeignKey("admins.id"),unique=True)

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    points = Column(Integer, default=0)

    # Relationship to Admin
    admin: Mapped["Admin"] = relationship("Admin", back_populates="user")
    hunger_pins = relationship("HungerPin", back_populates="pinned_by")



class FoodPost(Base):
    __tablename__ = "foodpost"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String(255), nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"))
    status = Column(String(20), default="AVAILABLE")

    created_at = Column(DateTime, default=datetime.utcnow)

class Claim(Base):
    __tablename__="claim"

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)

    food_id:Mapped[int]=mapped_column(Integer,ForeignKey("foodpost.id"))
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey("user.id"))

    status:Mapped[str]=mapped_column(String,default="CLAIMED")

    claimed_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
