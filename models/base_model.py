#!/usr/bin/python3
"""
Contains class BaseModel
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self):
        """
        Initializes BaseModel class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of BaseModel class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        update the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
