from sqlalchemy.orm import Session

from models.restaurant import Restaurant


def get_all_restaurants(db: Session):
    return db.query(Restaurant).all()
