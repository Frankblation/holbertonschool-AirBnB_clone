#!/usr/bin/python3
"""User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User.

    Attributes:
        email: the email of the user (str)
        password: The password of the user (str)
        first_name: The first name of the user (str)
        last_name: The last name of the user (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
