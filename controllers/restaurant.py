from sqlalchemy.orm import Session

from models.restaurant import Restaurant


def get_all_restaurants(db: Session):
    return db.query(Restaurant).all()


def get_restaurant(db: Session, restaurant_id: int):
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()


def create_restaurant(db: Session, restaurant):
    try:
        db_restaurant = Restaurant(**restaurant.dict())
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        return db_restaurant
    except Exception:
        db.rollback()
        return None


def update_restaurant(db: Session, restaurant_id: int, restaurant):
    try:
        db_restaurant = db.query(Restaurant).filter(
            Restaurant.id == restaurant_id).first()
        for var, value in restaurant:
            if value is not None:
                setattr(db_restaurant, var, value)
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        return db_restaurant
    except Exception:
        db.rollback()
        return None


def delete_restaurant(db: Session, restaurant_id: int):
    try:
        db_restaurant = db.query(Restaurant).filter(
            Restaurant.id == restaurant_id).first()
        db.delete(db_restaurant)
        db.commit()
        return db_restaurant
    except Exception:
        db.rollback()
        return None
