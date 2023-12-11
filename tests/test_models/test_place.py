#!/usr/bin/python3
"""Test place"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from models.place import place


class TestPlace(unittest.TestCase):

    def test_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_attribute_assignment(self):
        place = Place()
        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "Cozy Apartment"
        place.description = "A comfortable place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Cozy Apartment")

    def test_str_representation(self):
        place = Place(name="Spacious House", max_guest=6)
        str_representation = str(place)
        self.assertIn(place.__class__.__name__, str_representation)
        self.assertIn(place.id, str_representation)
        self.assertIn("name", str_representation)
        self.assertIn("Spacious House", str_representation)
        self.assertIn("max_guest", str_representation)
        self.assertIn("6", str_representation)

    def test_to_dict_method(self):
        place = Place(name="Modern Condo", max_guest=3)
        place_dict = place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["name"], "Modern Condo")
        self.assertEqual(place_dict["max_guest"], 3)


if __name__ == '__main__':
    unittest.main()
