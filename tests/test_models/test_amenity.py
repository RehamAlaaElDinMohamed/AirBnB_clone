#!/usr/bin/env python3
"""
    This is a module test from
    BaseModel class and your methods.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        this class test amenity class
    """

    def setUp(self):
        """
            Method set up, run before every test
        """
        self.amenity = Amenity()

    def test_creation(self):
        """
            test_creation: this test validates
            the creation of a Amenity must have
            a name with an empty string as default.
        """
        self.assertEqual(self.amenity.name, '')

    def test_Amenity(self):
        """
            test_Amenity: this test validates validate
            if a Amenity has a name then it must have
            the same name othorwise an error is raised
        """
        amenity = Amenity()
        amenity.name = "WIFI"
        self.assertEqual(amenity.name, "WIFI")
