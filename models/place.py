#!/usr/bin/python3
"""place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """place

        city_id (str): city id
        user_id (str): user id
        name (str): place name
        description (str): place context
        number_rooms (int): no. rooms
        number_bathrooms (int): no bathrooms
        max_guest (int): max no
        price_by_night (int): price
        latitude (float): place latitude
        longitude (float): place longitude
        amenity_ids (list): amenity list of id
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
