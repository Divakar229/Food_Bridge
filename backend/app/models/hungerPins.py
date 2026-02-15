from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .model import Base

class HungerPin(Base):
    __tablename__ = "hunger_pins"
    
    id = Column(Integer, primary_key=True, index=True)
    pinned_by_id = Column(Integer, ForeignKey("user.id"), nullable=True)  # note: table 'users' not 'user'
    address = Column(String, nullable=False)
    description = Column(String, nullable=True)
    likes = Column(Integer, default=0)
    served = Column(Boolean, default=False)         # boolean instead of integer
    resolved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)   # store when it was resolved or served
    served_at = Column(DateTime, nullable=True)

    pinned_by = relationship("User", back_populates="hunger_pins")