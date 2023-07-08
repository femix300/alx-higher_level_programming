#!/usr/bin/python3
"""unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A Class that defines unittests for max_integer([..])."""

    def test_positive_ordered_ints(self):
        """An ordered list of positive ints"""
        d_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(d_list), 4)

    def test_unordered_positive_ints(self):
        """A positive list that reads backwards"""
        d_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(d_list), 4)

    def test_negative_ordered_ints(self):
        """list of negative ints"""
        d_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(d_list), -1)

    def test_unordered_negative_ints(self):
        """A negative backwards list"""
        d_list = [-4, -3, -2, -1]
        self.assertEqual(max_integer(d_list), -1)

    def test_empty_list(self):
        """An empty list"""
        d_list = []
        self.assertEqual(max_integer(d_list), None)

    def test_none(self):
        """Test passing in only None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_args(self):
        """Pass no args into the function"""
        self.assertIsNone(max_integer())

    def test_2d_list(self):
        """Tests a 2d list"""
        d_list = [[2, 7], [8, 9]]
        self.assertEqual(max_integer(d_list), [8, 9])

    def test_ints_and_floats(self):
        """Tests ints and floats"""
        d_list = [4, 56.7, 3.92]
        self.assertEqual(max_integer(d_list), 56.7)

    def test_strings(self):
        """Tests strings passed into the func"""
        d_list = ["Peter", "Food", "Achievements"]
        self.assertEqual(max_integer(d_list), "Peter")

    def test_float(self):
        """Tests only floats in the function"""
        d_list = [2.5, 18.97, 300.2, 1000.15]
        self.assertEqual(max_integer(d_list), 1000.15)


if __name__ == '__main__':
    unittests.main()
