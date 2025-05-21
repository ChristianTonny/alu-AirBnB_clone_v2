#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            # Attributes that can be set via kwargs for any BaseModel
            # derivative. This includes Columns defined in subclasses.
            # Get class-level attributes  #  Ensure two spaces before comment
            allowed_keys = set(self.__class__.__dict__.keys())
            # Add instance-level attributes that might be set before this
            # loop by a superclass or similar.
            # For BaseModel itself, primary ones are id, created_at,
            # updated_at. This check needs to be robust for inheritance.

            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                # Check if the key is a legitimate attribute to set.
                # Legit: id, created_at, updated_at, or any Column name
                # in class.
                if key not in ['id', 'created_at', 'updated_at'] and \
                   not hasattr(self.__class__, key):
                    # If it's not a base known key and not a class
                    # attribute (like a Column).
                    # Then it's an unexpected kwarg for this model type.
                    raise KeyError(
                        f"Invalid attribute '{key}' for "
                        f"class {self.__class__.__name__}"
                    )

                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(
                        value,
                        '%Y-%m-%dT%H:%M:%S.%f'
                    )
                setattr(self, key, value)

            # Set default values if not provided in kwargs
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)
