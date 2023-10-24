#!/usr/bin/python3
"""State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
        name: The name of the state (str)
    """

    name = ""
