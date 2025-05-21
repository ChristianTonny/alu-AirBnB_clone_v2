#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        Args:
            cls (class, optional): Class to filter objects by
        """
        if cls is not None:
            filtered_dict = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    filtered_dict[key] = value
            return filtered_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside
        Args:
            obj (obj, optional): Object to delete
        """
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            FileStorage.__objects = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp_load_dict = json.load(f)
                for key, val_dict in temp_load_dict.items():
                    cls = classes[val_dict['__class__']]
                    FileStorage.__objects[key] = cls(**val_dict)
        except FileNotFoundError:
            pass
