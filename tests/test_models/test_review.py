#!/usr/bin/python3
"""Test Review"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Review class"""

    def test_instantiation(self):
        model = Review()
        self.assertIs(type(model), Review)

        model.text = "5-stars"
        self.assertEqual([model.text],["5-stars"])

    def test_subclass(self):
        model = Review()
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(isinstance(model, BaseModel))

    def test_attributes(self):
        model = Review()
        self.assertTrue(hasattr(model, "text"))
        self.assertEqual(model.text, "")
        self.assertTrue(hasattr(model, "place_id"))
        self.assertEqual(model.place_id, "")
        self.assertTrue(hasattr(model, "user_id"))
        self.assertEqual(model.user_id, "")

    def test_to_dict(self, mock_storage):
        model = Review()
        model.text = "review"
        rdict = model.to_dict()
        self.assertEqual(rdict["__class__"], "Review")
        self.assertEqual(str(model.id), rdict["id"])
        self.assertEqual(model.__dict__["created_at"].isoformat(),
                         rdict["created_at"])
        self.assertEqual(model.__dict__["updated_at"].isoformat(),
                         rdict["updated_at"])
        self.assertEqual(model.__dict__["text"],rdict["text"])


if __name__ == '__main__':
    unittest.main()
