import statistics
from sqlalchemy.orm import Session
from geoalchemy2 import functions as geo_func

from models.restaurant import Restaurant
from services.restaurant_importer import RestaurantImporter, RestaurantImporterService


def get_all_restaurants(db: Session):
    return db.query(Restaurant).all()


def get_restaurant(db: Session, restaurant_id: str):
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()


def create_restaurant(db: Session, restaurant):
    try:
        db_restaurant = Restaurant(
            id=restaurant.id,
            rating=restaurant.rating,
            name=restaurant.name,
            site=restaurant.site,
            email=restaurant.email,
            phone=restaurant.phone,
            street=restaurant.street,
            city=restaurant.city,
            state=restaurant.state,
            latitude=restaurant.latitude,
            longitude=restaurant.longitude,
            geom=geo_func.ST_SetSRID(
                geo_func.ST_MakePoint(
                    restaurant.longitude, restaurant.latitude),
                4326  # SRID for WGS 84
            )
        )
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        return db_restaurant
    except Exception as e:
        print(e)
        db.rollback()
        return None


def update_restaurant(db: Session, restaurant_id: str, restaurant):
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


def delete_restaurant(db: Session, restaurant_id: str):
    try:
        db_restaurant = db.query(Restaurant).filter(
            Restaurant.id == restaurant_id).first()
        db.delete(db_restaurant)
        db.commit()
        return db_restaurant
    except Exception:
        db.rollback()
        return None


def import_restaurants(db: Session, file):
    try:
        restaurant_importer = RestaurantImporter(file)
        restaurant_importer_service = RestaurantImporterService(
            restaurant_importer.get_dataframe())
        data_count = restaurant_importer_service.save_data()
        restaurant_importer_service.session.close()
        if data_count is False:
            return False
        return data_count
    except Exception as e:
        print(e)
        return False


def get_restaurants_statistics(
    db: Session,
    latitude: float,
    longitude: float,
    radius: float
):
    # Create a point geometry for the center of the circle
    center_point = geo_func.ST_SetSRID(
        geo_func.ST_MakePoint(longitude, latitude),
        4326  # SRID for WGS 84
    )

    # Query restaurants within the specified radius
    restaurants_within_radius = (
        db.query(Restaurant)
        .filter(
            geo_func.ST_DWithin(Restaurant.geom, center_point, radius)
        )
        .all()
    )

    if not restaurants_within_radius:
        return {
            "count": 0,
            "avg": 0.0,
            "std": 0.0,
        }

    # Calculate statistics
    ratings = [r.rating for r in restaurants_within_radius]
    count = len(restaurants_within_radius)
    avg = sum(ratings) / count
    std = statistics.stdev(ratings) if count > 1 else 0.0

    return {
        "count": count,
        "average_rating": avg,
        "standard_deviation": std,
    }
