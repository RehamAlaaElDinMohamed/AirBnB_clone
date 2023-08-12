#!/usr/bin/env python3
"""
    This is a module test from
    BaseModel class and your methods.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
        this class test City class
    """

    def setUp(self):
        """
            Method set up, run before every test
        """
        self.city = City()

    def test_creation(self):
        """
            test_creation: this test validates
            the creation of a City must have
            a name with an empty string as default.
        """
        self.assertEqual(self.City.name, '')

    def test_City(self):
        """
            test_City: this test validates validate
            if a City has a name then it must have
            the same name othorwise an error is raised
        """
        City = City()
        City.name = "Nasir City"
        self.assertEqual(City.name, "Nasir City")
