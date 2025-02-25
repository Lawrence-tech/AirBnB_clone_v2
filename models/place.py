#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
        city_id: id for city
        user_id: user's id
        name: name of the place
        description: places' decription
        number_rooms: room numbers
        number_bathrooms: number of bathrooms
        max_guest: maximum number of guests
        price_by_night: Cost per night
        latitude: latitude of the place
        longitude: longitude of the place
        amenity_ids: Place id
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Integer, nullable=True)
    longitude = Column(Integer, nullable=True)
    amenity_ids = []
