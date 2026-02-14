from fastapi import Depends,APIRouter,HTTPException,status
from typing import Annotated

from ..schemas.HungerPins import HungerPinCreate,HungerPinResponse
from ..routes.user import db_depends
from ..crud import curd_pins



router=APIRouter(
    prefix="/HungerPins",
    tags=["HengerPins"]
)

@router.post("/",response_model=HungerPinResponse)
def create_pin(db:db_depends,pin:HungerPinCreate):
    return curd_pins.point_pin(db,pin)
