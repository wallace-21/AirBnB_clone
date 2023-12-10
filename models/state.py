#!/usr/bin/python3
"""Defines state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

        name (str): state name
    """

    name = ""
