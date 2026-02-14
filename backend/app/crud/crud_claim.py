from fastapi import HTTPException,status,Depends
from datetime import datetime
from ..models.model import Claim
from sqlalchemy.orm import Session
from ..core.dependencies import get_current_admin
from ..models.admin import Admin
from ..models.model import FoodPost

def create_claim(db: Session, food_id: int, user_id: int):

    food = db.query(FoodPost).filter(FoodPost.id == food_id).first()

    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    if food.status != "AVAILABLE":
        raise HTTPException(status_code=400, detail="Food not available")

    claim = Claim(
        food_id=food_id,
        user_id=user_id,
        status="CLAIMED",
        claimed_at=datetime.utcnow()
    )

    db.add(claim)

    food.status = "CLAIMED"

    db.commit()
    db.refresh(claim)

    return claim