
from sqlalchemy.orm import Session
from ..models.model import FoodPost
from ..schemas.schema import FoodCreate as FoodSchema
from backend.app.utils.geocode import get_lat_lng


from ..models.model import User
from .food_constants import get_food_type, calculate_points


def foodPost(db:Session,fp:FoodSchema,user_id:int):
    lat, lng = get_lat_lng(fp.address)
    if lat is None:
        raise ValueError("Invalid address")
    
      # Use title as the item
    item_name = fp.title

    # Determine food type automatically
    # food_type = get_food_type(item_name)

    food_post = FoodPost(
        title=fp.title,
        quantity=fp.quantity,
        address=fp.address,
        latitude=lat,
        longitude=lng,
        user_id=user_id)
    db.add(food_post)
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        points = calculate_points(item_name, fp.quantity)
        user.points += points
    else:
        points = 0
    db.commit()
    db.refresh(food_post)
    return {
        "food_post": food_post,
        "points_earned": points,
        "total_user_points": user.points if user else 0
    }

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

