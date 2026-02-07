from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Literal


class CustomBaseModel(BaseModel):
    class Config:
        from_attributes = True       # ORM → Pydantic
        validate_assignment = True
        extra = "ignore"


class User(CustomBaseModel):
    name: str
    role: Literal["DONOR", "FOUNDATION", "RECEIVER"]
    phone: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserResponse(CustomBaseModel):
    id: UUID
    name: str
    role: Literal["DONOR", "FOUNDATION", "RECEIVER"]
    phone: str
    created_at: datetime


class FoodPost(CustomBaseModel):
    id: int
    title: str
    quantity: int
    latitude: float
    longitude: float
    address: str
    posted_by: UUID
    status: Literal["AVAILABLE", "CLAIMED", "DISTRIBUTED"]
    is_donated: bool
    created_at: datetime | None = None   # LET ORM FILL THIS


class FoodPostResponse(CustomBaseModel):
    id: int
    title: str
    status: str


class Claim(CustomBaseModel):
    id: int
    food_id: int
    claimed_by: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Distribution(CustomBaseModel):
    id: int
    food_id: int
    latitude: float
    longitude: float
    distributed_at: datetime = Field(default_factory=datetime.utcnow)
