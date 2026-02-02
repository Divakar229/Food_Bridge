from pydantic import BaseModel,Field  #(field is used to add extra features to a attribute)
from uuid import UUID, uuid4
from datetime import datetime
from typing import Literal

class CustomBaseModel(BaseModel):
    class config:
        from_attributes:True   #--># allows reading data from ORM objects
        validate_assignment=True  #-->to validate data after the creation
        extra="ignore"   #-->ignores the extra data send by the user

class User(CustomBaseModel):
    id:UUID=Field(default_factory=uuid4)
    name:str
    status: Literal["AVAILABLE", "CLAIMED", "DISTRIBUTED"]   # restriction to set of options
    phone:str
    created_at:datetime=Field(default_factory=datetime.utcnow())

class FoodPost(CustomBaseModel):
    id:int
    title:str
    quantity:int
    latitude:float
    longitude:float
    address:str
    status: Literal["AVAILABLE", "CLAIMED", "DISTRIBUTED"]
    posted_by:UUID #user_id of the donor
    created_at:datetime=Field(default_factory=datetime.utcnow())
    is_donated:(bool) 

class Claim(CustomBaseModel):
    id:int
    food_id:int
    claimed_by:UUID
    created_at:datetime=Field(default_factory=datetime.utcnow())


class Distribution(CustomBaseModel):
    id:int
    food_id:int
    latitude:float
    longitude:float
    distributed_at:datetime = Field(default_factory=datetime.utcnow)