from pydantic import BaseModel


class RestaurantBase(BaseModel):
    id: str
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


class RestaurantCreate(RestaurantBase):
    pass


class Restaurant(RestaurantBase):
    internal_id: int

    class Config:
        orm_mode = True


class RestaurantUpdate(BaseModel):
    rating: int | None = None
    name: str | None = None
    site: str | None = None
    email: str | None = None
    phone: str | None = None
    street: str | None = None
    city: str | None = None
    state: str | None = None
    latitude: float | None = None
    longitude: float | None = None


class RestaurantImportResponse(BaseModel):
    total_imported: int
