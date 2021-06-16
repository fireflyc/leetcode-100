import unittest
from leetcode.stella import Array


class ArrayTestCase(unittest.TestCase):
    def test_find_the_distance_value_between_two_arrays(self):
        find_distance = Array.find_the_distance_value_between_two_arrays
        self.assertEqual(2, find_distance(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
