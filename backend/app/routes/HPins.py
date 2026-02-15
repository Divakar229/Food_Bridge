from fastapi import Depends,APIRouter,HTTPException,status
from typing import List

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

@router.get("/", response_model=List[HungerPinResponse])
def get_pins(db: db_depends):
    return db.query(curd_pins.HP).all()

@router.get("/{pin_id}", response_model=HungerPinResponse)
def get_pin(pin_id: int, db: db_depends):
    return curd_pins.get_pin(pin_id,db)


@router.patch("/{pin_id}/update_status", response_model=HungerPinResponse)
def update_status(
    db: db_depends,
    pin_id: int,
    served: bool | None = None,
    resolved: bool | None = None,
):
    return curd_pins.update_status(pin_id,db,resolved, served)


@router.patch("/{pin_id}/like", response_model=None)
def like_pin(pin_id: int, db: db_depends):  # user_id from auth ideally
    return curd_pins.like_pin(pin_id,db)

@router.delete("/{pin_id}", response_model=None)
def delete_pin(pin_id: int, db: db_depends):
    return curd_pins.delete_pin(pin_id,db)


