#!/usr/bin/python3
"""Unit tests for console create command with parameters."""
import unittest
from unittest.mock import patch
from io import StringIO
import os
#  import json  # Not strictly needed for these tests
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.state import State
from models.place import Place
from models.user import User


class TestConsoleCreateParams(unittest.TestCase):
    """Test cases for the HBNB console's create command with parameters."""

    def setUp(self):
        """Set up test environment before each test."""
        # Ensure clean environment for FileStorage
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        self.console = HBNBCommand()
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up test environment after each test."""
        # Clean up FileStorage file
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        FileStorage._FileStorage__objects = {}

    def test_create_state_with_name(self):
        """Test creating a State with the name parameter."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            state_id = f.getvalue().strip()
        self.assertTrue(len(state_id) > 0)
        key = "State." + state_id
        self.assertIn(key, FileStorage._FileStorage__objects)
        obj_name = FileStorage._FileStorage__objects[key].name
        self.assertEqual(obj_name, "California")

    def test_create_state_with_name_underscore(self):
        """Test State creation with a name containing underscores."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="New_York"')
            state_id = f.getvalue().strip()
        self.assertTrue(len(state_id) > 0)
        key = "State." + state_id
        self.assertIn(key, FileStorage._FileStorage__objects)
        obj_name = FileStorage._FileStorage__objects[key].name
        self.assertEqual(obj_name, "New York")

    def test_create_place_multiple_params(self):
        """Test creating a Place with multiple varied parameters."""
        cmd_str = (
            'create Place city_id="0001" user_id="0001" '
            'name="My_little_house" number_rooms=4 number_bathrooms=2 '
            'max_guest=10 price_by_night=300 latitude=37.773972 '
            'longitude=-122.431297'
        )
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(cmd_str)
            place_id = f.getvalue().strip()

        self.assertTrue(len(place_id) > 0)
        key = "Place." + place_id
        self.assertIn(key, FileStorage._FileStorage__objects)
        place = FileStorage._FileStorage__objects[key]

        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.user_id, "0001")
        self.assertEqual(place.name, "My little house")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 300)
        self.assertEqual(place.latitude, 37.773972)
        self.assertEqual(place.longitude, -122.431297)

    def test_create_with_invalid_param_syntax(self):
        """Test create with invalid parameters that should be skipped."""
        command = ('create User name="John" age=invalid_int '
                   'email="test@test.com"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(command)
            user_id = f.getvalue().strip()

        self.assertTrue(len(user_id) > 0)
        key = "User." + user_id
        self.assertIn(key, FileStorage._FileStorage__objects)
        user = FileStorage._FileStorage__objects[key]

        self.assertEqual(user.name, "John")
        self.assertEqual(user.email, "test@test.com")
        self.assertFalse(hasattr(user, "age"))

    def test_create_string_with_escaped_quote(self):
        """Test create with a string parameter containing escaped quotes."""
        cmd = 'create State name="Oregon_is_\\"the_best\\""'
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(cmd)
            state_id = f.getvalue().strip()

        self.assertTrue(len(state_id) > 0)
        key = "State." + state_id
        self.assertIn(key, FileStorage._FileStorage__objects)
        # Expected: underscores replaced, escaped quotes handled.
        obj_name = FileStorage._FileStorage__objects[key].name
        self.assertEqual(obj_name, 'Oregon is "the best"')

    def test_create_with_mixed_valid_and_malformed_params(self):
        """Test creation with a mix of valid and malformed parameters."""
        cmd_str = ('create Place name="Beach_House" rooms=3 '
                   'valid_float=3.14 malformed latitude=10.0')
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(cmd_str)
            obj_id = f.getvalue().strip()

        key = "Place." + obj_id
        self.assertIn(key, FileStorage._FileStorage__objects)
        obj = FileStorage._FileStorage__objects[key]

        self.assertEqual(obj.name, "Beach House")
        self.assertTrue(hasattr(obj, "latitude"))
        self.assertEqual(obj.latitude, 10.0)

        # Based on current do_create, these will be set
        self.assertTrue(hasattr(obj, "rooms"))
        self.assertEqual(obj.rooms, 3)
        self.assertTrue(hasattr(obj, "valid_float"))
        self.assertEqual(obj.valid_float, 3.14)
        self.assertFalse(hasattr(obj, "malformed"))


if __name__ == '__main__':
    unittest.main()
