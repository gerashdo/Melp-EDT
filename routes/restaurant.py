from fastapi import Depends, HTTPException
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
                description='Retrive all restaurants from the data base.')
def get_all_restaurants(db: Session = Depends(get_db)):
    return restaurant_controller.get_all_restaurants(db)


@restaurant.get("/restaurants/{restaurant_id}",
                response_model=restaurant_schema.Restaurant,
                tags=['restaurants'],
                description='Retrive a restaurant by id.')
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = restaurant_controller.get_restaurant(
        db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant
