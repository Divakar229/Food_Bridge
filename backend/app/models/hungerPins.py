from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .model import Base

class HungerPin(Base):
    __tablename__ = "hunger_pins"
    
    id = Column(Integer, primary_key=True, index=True)
    pinned_by_id = Column(Integer, ForeignKey("user.id"),nullable=True)
    address = Column(String, nullable=False)      
    description = Column(String, nullable=True)  
    likes = Column(Integer, default=0)          
    served = Column(Integer, default=0)          
    resolved = Column(Boolean, default=False)    
    timestamp = Column(DateTime, default=datetime.utcnow)

    pinned_by = relationship("User", back_populates="hunger_pins")
