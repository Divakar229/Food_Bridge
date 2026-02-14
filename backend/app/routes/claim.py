from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from backend.app.api.database import db_dependency
from ..crud import crud_claim
from ..crud import crud_food
from ..core.dependencies import get_current_admin
from ..models.model import User

db_depends = Annotated[Session, Depends(db_dependency)]

router = APIRouter(
    prefix="/claim",
    tags=["claim"]
)

@router.post("/{food_id}")
def claim_food(food_id: int,
               db: db_depends,
               current_admin= Depends(get_current_admin)):
    profile = current_admin.user
    if not profile:
        raise HTTPException(status_code=404, detail="Admin profile not found")
    # 1️⃣ Only FOUNDATION can claim
    if profile.role != "FOUNDATION":
        raise HTTPException(status_code=403, detail="Only foundation can claim food")

    # 2️⃣ Check food exists
    food = crud_food.get_food_by_id(db, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    # 3️⃣ Check availability
    if food.status != "AVAILABLE":
        raise HTTPException(status_code=400, detail="Food not available")

    return crud_claim.create_claim(db, food_id, profile.id)
