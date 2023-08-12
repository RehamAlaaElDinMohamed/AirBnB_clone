#!/usr/bin/env python3
"""
    This is a module test from
    BaseModel class and your methods.
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
        this class test Review class
    """

    def setUp(self):
        """
            Method set up, run before every test
        """
        self.review = Review()

    def test_creation(self):
        """
            test_creation: this test validates
            the creation of a Review must have
            a name with an empty string as default.
        """
        self.assertEqual(self.review.text, '')

    def test_Review(self):
        """
            test_Review: this test validates
            validate if a Review has a name
            then it must have the same name
            othorwise an error is raised
        """
        review = Review()
        review.text = "Nasir Review"
        self.assertEqual(review.text, "Nasir Review")
