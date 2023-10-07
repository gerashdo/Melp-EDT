from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter

from config.db import SessionLocal
import controllers.restaurant as restaurant_controller
import schemas.restaurant as restaurant_schema


restaurant = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@restaurant.get("/restaurants",
                response_model=list[restaurant_schema.Restaurant],
                tags=['restaurants'],
                description='Retrive al the restaurants from the data base.')
def get_all_restaurants(db: Session = Depends(get_db)):
    return restaurant_controller.get_all_restaurants(db)
