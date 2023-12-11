#!/usr/bin/python3
"""Test user"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from models.user import user


class TestUser(unittest.TestCase):

    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attribute_assignment(self):
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_str_representation(self):
        user = User(email="user@example.com",
                    first_name="John", last_name="Doe")
        str_representation = str(user)
        self.assertIn(user.__class__.__name__, str_representation)
        self.assertIn(user.id, str_representation)
        self.assertIn("email", str_representation)
        self.assertIn("user@example.com", str_representation)
        self.assertIn("first_name", str_representation)
        self.assertIn("John", str_representation)
        self.assertIn("last_name", str_representation)
        self.assertIn("Doe", str_representation)

    def test_to_dict_method(self):
        user = User(email="user@example.com",
                    first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "user@example.com")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")


if __name__ == '__main__':
    unittest.main()
