from sqlalchemy.orm import Session

from models.restaurant import Restaurant


def get_all_restaurants(db: Session):
    return db.query(Restaurant).all()


def get_restaurant(db: Session, restaurant_id: int):
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
