#!/usr/bin/python3
"""Tests for BaseModel"""

import unittest
import uuid
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestState(unittest.TestCase):
    """Test the BaseModel class"""

    def test_instantiation(self):
        model = State()
        self.assertIs(type(model), State)

        model.name = "Texas"
        self.assertEqual([model.name,["chii"])

    def test_attributes(self):
        model = State()
        self.assertTrue(hasattr(model, "name"))
        self.assertEqual(model.name, "")

    def test_to_dict(self):
        model = State()
        model.name = "Texas"
        sdict = model.to_dict()
        self.assertEqual(sdict["__class__"], "State")
        self.assertEqual(str(model.id), sdict["id"])
        self.assertEqual(model.__dict__["created_at"].isoformat(),
                         sdict["created_at"])
        self.assertEqual(model.__dict__["updated_at"].isoformat(),
                         sdict["updated_at"])
        self.assertEqual(model.__dict__["name"],
                         sdict["name"])


if __name__ == '__main__':
    unittest.main()
