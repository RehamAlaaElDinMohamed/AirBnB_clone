#!/usr/bin/env python3
"""
    This is a module test from
    BaseModel class and your methods.
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
        this class test Place class
    """

    def setUp(self):
        """
            Method set up, run before every test
        """
        self.place = Place()

    def test_creation(self):
        """
            test_creation: this test validates
            the creation of a Place must have
            a name with an empty string as default.
        """
        self.assertEqual(self.place.name, '')

    def test_Place(self):
        """
            test_Place: this test validates validate
            if a Place has a name then it must have
            the same name othorwise an error is raised
        """
        place = Place()
        place.name = "Room no 007"
        self.assertEqual(place.name, "Room no 007")
