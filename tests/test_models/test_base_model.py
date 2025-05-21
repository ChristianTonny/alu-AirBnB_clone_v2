#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import time


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = self.value(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = self.value(**copy)

    def test_save(self):
        """ Testing the save method for different storage types. """
        i = self.value()
        i.save()
        key = self.name + "." + i.id

        storage_type = os.getenv('HBNB_TYPE_STORAGE')

        if storage_type == 'file':
            self.assertTrue(os.path.exists('file.json'),
                            "file.json should exist after save for FileStorage")
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())
        elif storage_type == 'db':
            # For DB, check if the object can be retrieved from storage.
            # This assumes 'i' is a new object that should be in storage after save.
            from models import storage as current_storage # Renamed to avoid conflict
            retrieved_obj = current_storage.all(self.value).get(key)
            self.assertIsNotNone(retrieved_obj,
                                 f"{self.name} instance not found in DB after save")
            self.assertEqual(retrieved_obj.id, i.id)
            # Optionally, add more specific database assertions here,
            # such as querying the database directly to verify the commit.
        else: # Default to FileStorage behavior if HBNB_TYPE_STORAGE is not set
            if not storage_type: # Or if you prefer explicit check for None or empty
                self.assertTrue(os.path.exists('file.json'),
                                "file.json should exist (default FS check)")
                with open('file.json', 'r') as f:
                    j = json.load(f)
                    self.assertEqual(j[key], i.to_dict())
            # else: # If storage_type is set but not 'file' or 'db'
            #     pass # Or raise an error, or log a warning, depending on desired behavior

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        # Ensure updated_at is different from created_at by saving
        time.sleep(0.001) # Ensure time moves
        new.save()
        n = new.to_dict()
        reloaded_new = self.value(**n)
        self.assertFalse(reloaded_new.created_at == reloaded_new.updated_at)
