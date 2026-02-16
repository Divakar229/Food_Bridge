from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema for creating a pin
class HungerPinCreate(BaseModel):
    address: str
    description: Optional[str] = None

# Schema for updating resolved status
class HungerPinUpdate(BaseModel):
    resolved: bool

# Schema for like/serve action (just incremental, no extra data needed)
class HungerPinAction(BaseModel):
    pass  # You can leave empty, or include optional user info if needed

# Response schema
class HungerPinResponse(BaseModel):
    id: int
    address: str
    description: Optional[str]
    likes: int
    served: bool
    resolved: bool
    created_at: datetime
    resolved_at: Optional[datetime]
    served_at: Optional[datetime]
    user_name: Optional[str] = None 


    class Config:
        from_atrributes=True
