from pydantic import BaseModel


class RestaurantBase(BaseModel):
    rating: int
    name: str
    site: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    latitude: float
    longitude: float


class Restaurant(RestaurantBase):
    id: int

    class Config:
        orm_mode = True
