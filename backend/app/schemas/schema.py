from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class CustomBaseModel(BaseModel):
    class Config:
        from_attributes = True       # ORM → Pydantic
        validate_assignment = True
        extra = "ignore"


class UserCreate(CustomBaseModel):
    name: str
    role: Literal["DONOR", "FOUNDATION", "RECEIVER"]
    phone: str


class UserResponse(CustomBaseModel):
    id: int
    name: str
    role: Literal["DONOR", "FOUNDATION", "RECEIVER"]
    phone: str
    created_at: datetime


class FoodCreate(CustomBaseModel):
    title: str
    quantity: int
    address: str


class FoodResponse(CustomBaseModel):
    id: int
    title: str
    quantity: int
    latitude: float
    longitude: float
    address: str
    user_id: int
    status: Literal["AVAILABLE", "CLAIMED", "DISTRIBUTED"]
    created_at: datetime


class Claim(CustomBaseModel):
    id:int
    food_id:int
    user_id:int
    status:str
    claimed_at:datetime
