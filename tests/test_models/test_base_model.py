#!/usr/bin/python3
"""Tests for BaseModel"""

import unittest
import uuid
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_instantiation(self):
        model = BaseModel()
        self.assertIs(type(model), BaseModel)

        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model.name = "chii"
        model.number = 78
        self.assertEqual([my_model.name, my_model.number],
                         ["chii", 78])

    def test_attributes(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_two_models_different_updated_at(self):
        model = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model.updated_at, model2.updated_at)

    def test_str(self):
        model = BaseModel()
        string = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(string, str(model))

    def test_uuid(self):
        model = BaseModel()
        uuid_obj = uuid.uuid4(model.id)
        self.assertEqual(str(uuid_obj), model.id)

        model2 = BaseModel()
        my_id = model2.id
        uuid_obj = uuid.uuid4(my_id)
        self.assertIs(type(uuid_obj), uuid.uuid4)

    def test_to_dict(self):
        model2 = BaseModel()
        my_dict = model2.to_dict()
        self.assertIs(type(my_dict), dict)

        model = BaseModel()
        model.name = "chii"
        model.number = 378
        model_dict = model.to_dict()
        self.assertIs(type(model_dict), dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], 'chii')
        self.assertEqual(model_dict['number'], 378)
        self.assertIs(type(model_dict['created_at']), str)
        self.assertIs(type(model_dict['updated_at']), str)

    def test_to_dict_values(self):
        model = BaseModel()
        model.name = "chii"
        model.number = 378
        my_dict = model.to_dict()
        expected_dict = {
            "id": model.id,
            "created_at": model.created_at.isoformat(),
            "updated_at": model.updated_at.isoformat(),
            "name": "chii",
            "number": 378,
            "__class__": model.__class__.__name__
        }
        self.assertDictEqual(expected_dict, my_dict)

        model2 = BaseModel()
        model2.name = "chii"
        model2.number = 378
        my_model_dict = model2.to_dict()
        self.assertEqual(my_model_dict['name'], 'chii')
        self.assertEqual(my_model_dict['number'], 378)


if __name__ == '__main__':
    unittest.main()
