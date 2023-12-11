#!/usr/bin/python3
"""Test City"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from models.city import City


class TestCity(unittest.TestCase):
    """City class"""

    def test_instantiation(self):
        model = City()
        self.assertIs(type(model), City)

        my_city.name = "Pretoria"
        self.assertEqual([model.name],["Pretoria"])

    def test_subclass(self):
        models = City()
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(isinstance(model, BaseModel))

    def test_attributes(self):
        model = City()
        self.assertTrue(hasattr(model, "name"))
        self.assertEqual(model.name, "")
        self.assertTrue(hasattr(model, "state_id"))
        self.assertEqual(model.name, "")

    def test_to_dict(self, mock_storage):
        model = City()
        models.name = "Barcelona"
        cdict = model.to_dict()
        self.assertEqual(cdict["__class__"], "City")
        self.assertEqual(str(model.id), cdict["id"])
        self.assertEqual(model.__dict__["created_at"].isoformat(),
                         cdict["created_at"])
        self.assertEqual(model.__dict__["updated_at"].isoformat(),
                         cdict["updated_at"])
        self.assertEqual(model.__dict__["name"],
                         cdict["name"])


if __name__ == '__main__':
    unittest.main()
