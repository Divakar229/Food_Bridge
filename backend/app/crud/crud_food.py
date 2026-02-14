
from sqlalchemy.orm import Session
from ..models.model import FoodPost
from ..schemas.schema import FoodCreate as FoodSchema
from backend.app.utils.geocode import get_lat_lng


def foodPost(db:Session,fp:FoodSchema,user_id:int):
    lat, lng = get_lat_lng(fp.address)
    if lat is None:
        raise ValueError("Invalid address")

    food_post = FoodPost(
        title=fp.title,
        quantity=fp.quantity,
        address=fp.address,
        latitude=lat,
        longitude=lng,
        user_id=user_id)
    db.add(food_post)
    db.commit()
    db.refresh(food_post)
    return food_post

def avaliability(db:Session):
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

def get_all_food(
    db:Session,
    skip: int = 0,
    limit: int = 10
):
    return db.query(FoodPost).offset(skip).limit(limit).all()


def distribute_food(db: Session, food_id: int):
    food = db.query(FoodPost).filter(FoodPost.id == food_id).first()
    if not food:
        return None
    food.status = "DISTRIBUTED"
    db.commit()
    db.refresh(food)
    return food

