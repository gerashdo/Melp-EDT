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


@restaurant.get("/restaurants/",
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


@restaurant.post("/restaurants/", response_model=restaurant_schema.Restaurant)
def create_restaurant(restaurant: restaurant_schema.RestaurantCreate, db: Session = Depends(get_db)):
    new_restaurant = restaurant_controller.create_restaurant(
        db=db, restaurant=restaurant)
    if new_restaurant is None:
        raise HTTPException(
            status_code=500, detail="Restaurant could not be created, contact the administrator.")
    return new_restaurant


@restaurant.put("/restaurants/{restaurant_id}",
                response_model=restaurant_schema.Restaurant,
                tags=['restaurants'],
                description='Update a restaurant by id.')
def update_restaurant(restaurant_id: int, restaurant: restaurant_schema.RestaurantUpdate, db: Session = Depends(get_db)):
    restaurant_to_update = restaurant_controller.get_restaurant(
        db, restaurant_id=restaurant_id)
    if restaurant_to_update is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    updated_restaurant = restaurant_controller.update_restaurant(
        db=db, restaurant_id=restaurant_id, restaurant=restaurant)
    if updated_restaurant is None:
        raise HTTPException(
            status_code=500, detail="Restaurant could not be updated, contact the administrator.")
    return updated_restaurant
