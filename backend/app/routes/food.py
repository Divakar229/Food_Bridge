from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
import logging

from typing import Annotated
from backend.app.api.database import db_dependency
from ..schemas.schema import FoodPost,FoodPostResponse
from ..curd import crud_food

db_depends=Annotated[Session,Depends(db_dependency)]

logger=logging.getLogger(__name__)


router=APIRouter(
    prefix="/food",
    tags=["food"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_post(db:db_depends,f:FoodPost):
    logger.info("creating food post")

    return crud_food.foodPost(db,f)
logger.info("food post created successfully")

@router.get("/avalibilty",response_model=FoodPostResponse)
def Favaliblity(db:db_depends):
    return crud_food.avalibility(db)


@router.get("/{id}",response_model=FoodPostResponse)
def get_id(db:db_depends,id:int):
    return crud_food.get_food_by_id(db,id)

@router.put("/{id}/status",response_model=FoodPostResponse)
def updatePost(db:db_depends,id:int,new_status:str):
    return crud_food.update_food_status(db,id,new_status)


@router.delete("/{id}")
def deletePost(db:db_depends,id:int):
    logger.info("deleting the post")
    return crud_food.delete_food(db,id)
logger.info("the post successfully deleted")



