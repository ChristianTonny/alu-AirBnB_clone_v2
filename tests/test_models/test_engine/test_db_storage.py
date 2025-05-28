#!/usr/bin/python3
"""Unit tests for DBStorage engine."""
import unittest
import os
from unittest import skipIf
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


@skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
class TestDBStorage(unittest.TestCase):
    """Test cases for the DBStorage engine."""

    def setUp(self):
        """Set up test environment before each test."""
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """Clean up test environment after each test."""
        # Clean up any test data
        pass

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_all_no_class(self):
        """Test all() with no class specified."""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_all_with_class(self):
        """Test all() with a specific class."""
        result = self.storage.all(State)
        self.assertIsInstance(result, dict)

    def test_new(self):
        """Test new() method."""
        state = State(name="California")
        self.storage.new(state)
        # Check that the object is in the session
        self.assertIn(state, self.storage._DBStorage__session)

    def test_save(self):
        """Test save() method."""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        # After save, the object should have an ID
        self.assertIsNotNone(state.id)

    def test_delete(self):
        """Test delete() method."""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        state_id = state.id
        self.storage.delete(state)
        self.storage.save()
        # Check that the object is no longer in storage
        result = self.storage.all(State)
        self.assertNotIn(f"State.{state_id}", result)

    def test_delete_none(self):
        """Test delete() with None."""
        # Should not raise an error
        self.storage.delete(None)

    def test_reload(self):
        """Test reload() method."""
        # Should not raise an error
        self.storage.reload()

    def test_state_creation(self):
        """Test creating a State object."""
        state = State(name="Texas")
        self.storage.new(state)
        self.storage.save()
        self.assertIsNotNone(state.id)
        self.assertEqual(state.name, "Texas")

    def test_city_creation(self):
        """Test creating a City object."""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()

        city = City(name="San Francisco", state_id=state.id)
        self.storage.new(city)
        self.storage.save()
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.state_id, state.id)

    def test_user_creation(self):
        """Test creating a User object."""
        user = User(email="test@example.com", password="password")
        self.storage.new(user)
        self.storage.save()
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, "test@example.com")

    def test_place_creation(self):
        """Test creating a Place object."""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()

        city = City(name="San Francisco", state_id=state.id)
        self.storage.new(city)
        self.storage.save()

        user = User(email="test@example.com", password="password")
        self.storage.new(user)
        self.storage.save()

        place = Place(name="Test Place", city_id=city.id, user_id=user.id)
        self.storage.new(place)
        self.storage.save()
        self.assertIsNotNone(place.id)
        self.assertEqual(place.name, "Test Place")

    def test_amenity_creation(self):
        """Test creating an Amenity object."""
        amenity = Amenity(name="WiFi")
        self.storage.new(amenity)
        self.storage.save()
        self.assertIsNotNone(amenity.id)
        self.assertEqual(amenity.name, "WiFi")

    def test_review_creation(self):
        """Test creating a Review object."""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()

        city = City(name="San Francisco", state_id=state.id)
        self.storage.new(city)
        self.storage.save()

        user = User(email="test@example.com", password="password")
        self.storage.new(user)
        self.storage.save()

        place = Place(name="Test Place", city_id=city.id, user_id=user.id)
        self.storage.new(place)
        self.storage.save()

        review = Review(text="Great place!", place_id=place.id,
                        user_id=user.id)
        self.storage.new(review)
        self.storage.save()
        self.assertIsNotNone(review.id)
        self.assertEqual(review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
