#!/usr/bin/python3
""" BaseModel class."""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ base model of the airbnb clone"""
    def __init__(self):
        self.id = str(uuid4())
        self.create_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ string representation of name, id and dictionary"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.create_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
