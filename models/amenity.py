#!/usr/bin/python3
"""amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines an amenity.

    Attributes:
        name: The name of the amenity (str)
    """

    name = ""
