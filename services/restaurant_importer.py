from pandas import read_csv

from config.db import SessionLocal
from models.restaurant import Restaurant


class RestaurantImporter:
    def __init__(self, filename):
        self.dataframe = read_csv(filename)

    def get_dataframe(self):
        return self.dataframe


class RestaurantImporterService:
    def __init__(self, data):
        self.data = data
        self.session = SessionLocal()

    def save_data(self):
        try:
            restaurants = self._create_restaurants()
            self.session.add_all(restaurants)
            self.session.commit()
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
        return len(restaurants)

    def _create_restaurants(self):
        restaurants = []
        for _, row in self.data.iterrows():
            if not self._get_existing_restaurant(row):
                new_restaurant = self._create_restaurant_by_row(row)
                if not new_restaurant:
                    return False
                restaurants.append(new_restaurant)
        return restaurants

    def _create_restaurant_by_row(self, row):
        try:
            restaurant = Restaurant(
                id=row['id'],
                rating=row['rating'],
                name=row['name'],
                site=row['site'],
                email=row['email'],
                phone=row['phone'],
                street=row['street'],
                city=row['city'],
                state=row['state'],
                latitude=row['lat'],
                longitude=row['lng']
            )
            return restaurant
        except Exception as e:
            print(e)
            return None

    def _get_existing_restaurant(self, row):
        return self.session.query(Restaurant).filter(
            Restaurant.name == row['name'],
            Restaurant.site == row['site'],
            Restaurant.email == row['email'],
            Restaurant.phone == row['phone'],
            Restaurant.street == row['street'],
            Restaurant.city == row['city'],
            Restaurant.state == row['state'],
            Restaurant.latitude == row['lat'],
            Restaurant.longitude == row['lng']
        ).first()

    def _close_session(self):
        self.session.close()
