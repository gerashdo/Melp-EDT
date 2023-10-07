from sqlalchemy import Column, Integer, String, Float

from config.db import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    name = Column(String)
    site = Column(String)
    email = Column(String)
    phone = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
