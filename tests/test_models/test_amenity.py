#!/usr/bin/python3
"""Test amenity"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from models.amenity import amenity


class TestAmenity(unittest.TestCase):

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_name_assignment(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_str_representation(self):
        amenity = Amenity(name="Gym")
        str_representation = str(amenity)
        self.assertIn(amenity.__class__.__name__, str_representation)
        self.assertIn(amenity.id, str_representation)
        self.assertIn("name", str_representation)
        self.assertIn("Gym", str_representation)

    def test_to_dict_method(self):
        amenity = Amenity(name="Sauna")
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["name"], "Sauna")


if __name__ == '__main__':
    unittest.main()
