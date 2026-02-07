from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
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
    address = Column(String(255), nullable=False)

    posted_by = Column(UUID(as_uuid=True), nullable=False)

    status = Column(String(20), nullable=False, default="AVAILABLE")  
    is_donated = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
