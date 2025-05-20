#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """Amenity class that inherits from BaseModel and Base"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False, default="")

    def __init__(self, *args, **kwargs):
        """Initializes Amenity instance"""
        super().__init__(*args, **kwargs)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            if 'name' not in kwargs:
                self.name = ""
