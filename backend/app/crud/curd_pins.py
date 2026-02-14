from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import HungerPins
from ..models.hungerPins import HungerPin as HP
import logging

logger=logging.getLogger(__name__)



def point_pin(db:Session,pin:HungerPins.HungerPinCreate):
    existing_pin = db.query(HP).filter(HP.address==pin.address).first()
    if existing_pin:
        raise HTTPException(status_code=400, detail="Hunger pin already located")
    hpin=HP(**pin.dict())
    db.add(hpin)
    db.commit()
    db.refresh(hpin)
    logger.info(f"created a hunger pin at address:{pin.address}")
    return hpin

    
