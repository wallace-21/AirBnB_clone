#!/usr/bin/python3
"""city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """city

        state_id (str): state id
        name (str): city name
    """

    state_id = ""
    name = ""
