from fastapi import FastAPI

from config.db import engine
from models.restaurant import Base as RestaurantBase
from routes.restaurant import restaurant

RestaurantBase.metadata.create_all(bind=engine)

app = FastAPI(
    title="Melp API",
    description='API for restaurants information.',
    version="0.0.1",
    openapi_tags=[{
        "name": "melp",
        "description": "Restaurants endpoints."
    }]
)

app.include_router(restaurant)
