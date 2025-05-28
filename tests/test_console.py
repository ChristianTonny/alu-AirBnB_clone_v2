#!/usr/bin/python3
"""Unit tests for console module."""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.state import State
from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console."""

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

    def test_help(self):
        """Test help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue()
        self.assertIn("Documented commands", output)

    def test_quit(self):
        """Test quit command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF(self):
        """Test EOF command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            output = f.getvalue()
        self.assertEqual(output, "")

    def test_create_missing_class(self):
        """Test create command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create command with valid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            state_id = f.getvalue().strip()
        self.assertTrue(len(state_id) > 0)
        key = "State." + state_id
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_show_missing_class(self):
        """Test show command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show InvalidClass")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show command with invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State invalid_id")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy InvalidClass")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy State")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy State invalid_id")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_all_no_class(self):
        """Test all command with no class specified."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
        self.assertEqual(output, "[]")

    def test_all_invalid_class(self):
        """Test all command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all InvalidClass")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_class(self):
        """Test update command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update InvalidClass")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update State")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update command with invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update State invalid_id")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_count_command(self):
        """Test count command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count State")
            output = f.getvalue().strip()
        self.assertEqual(output, "0")

    def test_dot_notation_all(self):
        """Test dot notation for all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.all()")
            output = f.getvalue().strip()
        self.assertEqual(output, "[]")

    def test_dot_notation_count(self):
        """Test dot notation for count command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.count()")
            output = f.getvalue().strip()
        self.assertEqual(output, "0")


if __name__ == '__main__':
    unittest.main()
