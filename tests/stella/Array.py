import unittest
from leetcode.stella import Array


class ArrayTestCase(unittest.TestCase):
    def test_find_the_distance_value_between_two_arrays(self):
        find_distance = Array.find_the_distance_value_between_two_arrays
        self.assertEqual(2, find_distance(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))

    def test_rotate_matrix_lcci(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Array.rotate_matrix_lcci(data)
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], data)
        data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        Array.rotate_matrix_lcci(data)
        self.assertEqual([[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]], data)
