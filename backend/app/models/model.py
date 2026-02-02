from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from backend.app.api.database import declarative_base
from datetime import datetime
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class FoodPost(Base):
    __tablename__ = "foodpost"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True, index=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    status = Column(String(20), nullable=False, default="AVAILABLE")  # AVAILABLE / CLAIMED / DISTRIBUTED
    posted_by = Column(Integer, nullable=False)  # user_id of donor
    created_at = Column(DateTime, default=datetime.utcnow)
    is_donated = Column(Boolean, default=False)
