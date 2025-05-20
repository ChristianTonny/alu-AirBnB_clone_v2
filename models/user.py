#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False, default="")
    password = Column(String(128), nullable=False, default="")
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user",
                          cascade="all, delete-orphan")
    reviews = relationship("Review", backref="user",
                           cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initializes User instance"""
        super().__init__(*args, **kwargs)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            if 'email' not in kwargs:
                self.email = ""
            if 'password' not in kwargs:
                self.password = ""
            if 'first_name' not in kwargs:
                self.first_name = ""
            if 'last_name' not in kwargs:
                self.last_name = ""
