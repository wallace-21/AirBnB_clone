#!/usr/bin/python3
"""Defines user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User

        email (str): email
        password (str): user password
        first_name (str): user name
        last_name (str): user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
