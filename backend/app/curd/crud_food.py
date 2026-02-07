from sqlalchemy.orm import Session
from ..models.model import FoodPost
from ..schemas.schema import FoodPost as FoodSchema


def foodPost(db:Session,fp:FoodSchema):
    food_post=FoodPost(**fp.dict())
    db.add(food_post)
    db.commit()
    db.refresh(food_post)
    return food_post

def avalibility(db:Session):
    return db.query(FoodPost).filter(FoodPost.status=="AVAILABLE").all()

def get_food_by_id(db: Session, food_id: int):
    return db.query(FoodPost).filter(FoodPost.id == food_id).first()

def update_food_status(db: Session, food_id: int, new_status: str):
    food = db.query(FoodPost).filter(FoodPost.id == food_id).first()
    food.status = new_status
    db.commit()
    db.refresh(food)
    return food

def delete_food(db: Session, food_id: int):
    food = db.query(FoodPost).filter(FoodPost.id == food_id).first()
    db.delete(food)
    db.commit()
    return {"message": "Food post deleted successfully"}