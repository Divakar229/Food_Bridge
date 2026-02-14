from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
import logging

from typing import Annotated
from backend.app.api.database import db_dependency
from ..schemas.schema import FoodCreate,FoodResponse
from ..crud import crud_food
from ..core.dependencies import get_current_admin
db_depends=Annotated[Session,Depends(db_dependency)]

logger=logging.getLogger(__name__)


router=APIRouter(
    prefix="/food",
    tags=["food"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_post(db:db_depends,f:FoodCreate,current_user=Depends(get_current_admin)):
    logger.info("creating food post")

    return crud_food.foodPost(db,f,current_user.id)
logger.info("food post created successfully")

@router.get("/availability",response_model=list[FoodResponse])
def availability(db:db_depends):
    return crud_food.avaliability(db)


@router.get("/{id}",response_model=FoodResponse)
def get_id(db:db_depends,id:int):
    return crud_food.get_food_by_id(db,id)

@router.put("/{id}/status",response_model=FoodResponse)
def updatePost(db:db_depends,id:int,new_status:str):
    return crud_food.update_food_status(db,id,new_status)


@router.delete("/{id}")
def deletePost(db:db_depends,id:int):
    logger.info("deleting the post")
    return crud_food.delete_food(db,id)
logger.info("the post successfully deleted")

@router.get("/", response_model=list[FoodResponse])
def get_all_food(
    db: db_depends,
    skip: int = 0,
    limit: int = 10):
    return crud_food.get_all_food(db,skip,limit)

@router.patch("/{food_id}/distribute")
def distribute_food(food_id: int,
                    db: db_depends,
                    current_admin = Depends(get_current_admin)):

    food =crud_food.get_food_by_id(db, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    if food.status != "CLAIMED":
        raise HTTPException(status_code=400, detail="Food must be claimed first")

    return crud_food.distribute_food(db, food_id)




