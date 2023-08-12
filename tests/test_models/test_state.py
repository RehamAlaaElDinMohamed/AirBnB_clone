#!/usr/bin/env python3
"""
    This is a module test from
    BaseModel class and your methods.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
       this class test state class
    """

    def setUp(self):
        """
            Method set up, run before every test
        """
        self.state = State()

    def test_creation(self):
        """
            test_creation: this test validates
            the creation of a State must
            have a name with an empty string as default.
        """
        self.assertEqual(self.state.name, '')

    def test_state(self):
        """
            test_state: this test validates
            validate if a State has a name then
            it must have the same name othorwise an error is raised
        """
        state = State()
        state.name = "North Cairo"
        self.assertEqual(state.name, "North Cairo")
