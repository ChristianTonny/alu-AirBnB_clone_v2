#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        from models import storage_type  # Moved import here

        if storage_type == 'db':
            # For DBStorage, id, created_at, updated_at are handled by SQLAlchemy
            pass  # SQLAlchemy columns will be automatically managed
        else:
            # For FileStorage
            self.id = str(uuid.uuid4())  # Unique ID
            self.created_at = datetime.now()  # Creation timestamp
            self.updated_at = datetime.now()  # Update timestamp

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                                                         "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":  # Ignore __class__
                    # For FileStorage, set attributes directly.
                    # For DBStorage, this will set attributes on the SQLAlchemy model.
                    # If an attribute is not a mapped column in DBStorage,
                    # SQLAlchemy might ignore it or handle it based on its configuration.
                    setattr(self, key, value)

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
