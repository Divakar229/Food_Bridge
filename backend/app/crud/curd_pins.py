from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from datetime import timedelta,datetime
from sqlalchemy import or_,and_



from ..schemas import HungerPins
from ..models.hungerPins import HungerPin as HP
from ..models.model import User
import logging

logger=logging.getLogger(__name__)


def point_pin(pin: HungerPins.HungerPinCreate, db, admin_id: int):
    existing_pin = db.query(HP).filter(HP.address == pin.address).first()
    if existing_pin:
        raise HTTPException(status_code=400, detail="Hunger pin already located")

    hpin = HP(**pin.dict())
    db.add(hpin)

    # find the user whose admin_id matches current admin
    user = db.query(User).filter(User.admin_id == admin_id).first()
    if user:
        user.points += 2

    db.commit()
    db.refresh(hpin)
    return hpin





def get_pins(db:Session):
    return db.query(HP).all()

def get_pin(pin_id: int, db: Session):
    pin = db.query(HP).filter(HP.id == pin_id).first()
    if not pin:
        raise HTTPException(status_code=404, detail="Pin not found")
    return pin


def like_pin(pid_id:int,db:Session):
    pin=db.query(HP).filter(HP.id==pid_id).first()
    if not pin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="pin not found"
        )
    pin.likes += 1
    db.add(pin)
    db.commit()
    db.refresh(pin)
    return pin

def delete_pin(pid_id:int,db:Session):
    pin=db.query(HP).filter(HP.id==pid_id).first()
    if not pin:
        raise HTTPException(status_code=404, detail="Pin not found")
    db.delete(pin)
    db.commit()
    return {"detail":"pin deleted successfully"}

def update_status(pin_id: int, db: Session, resolved: bool = None, served: bool = None):
    pin = db.query(HP).filter(HP.id == pin_id).first()
    if not pin:
        raise HTTPException(status_code=404, detail="Pin not found")

    if resolved is None and served is None:
        raise HTTPException(status_code=400, detail="No status provided")

    if resolved:
        if pin.resolved:
            raise HTTPException(status_code=400, detail="Already resolved")
        pin.resolved = True
        pin.resolved_at = datetime.utcnow()

    if served:
        if pin.served:
            raise HTTPException(status_code=400, detail="Already served")
        pin.served = True
        pin.served_at = datetime.utcnow()

    db.commit()
    db.refresh(pin)
    return pin

def clean_old_pins(db: Session):
    cutoff = datetime.utcnow() - timedelta(minutes=2)

    old_pins = db.query(HP).filter(
        or_(
            and_(HP.resolved == True, HP.resolved_at <= cutoff),
            and_(HP.served == True, HP.served_at <= cutoff)
        )
    ).all()

    for pin in old_pins:
        db.delete(pin)

    db.commit()


def get_leaderboard(db: Session, page: int = 1, limit: int = 10):
    offset = (page - 1) * limit 
    users = (
        db.query(User)
        .order_by(User.points.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    
    return users

    
