#!/usr/bin/python3
"""Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes -
        city_id: the City id (str)
        user_id: the User id (str)
        name: he name of the place (str)
        description: the description of the place (str)
        number_rooms: the number of rooms of the place (int)
        number_bathrooms: the number of bathrooms of the place (int)
        max_guest: the maximum number of guests of the place (int)
        price_by_night: the price by night of the place (int)
        latitude: the latitude of the place (float)
        longitude: the longitude of the place (float)
        amenity_ids: a list of amenity ids (list)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
