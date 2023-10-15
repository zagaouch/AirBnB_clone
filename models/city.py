#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Represent a state

    Attributes:
        state_id (str): State id.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
