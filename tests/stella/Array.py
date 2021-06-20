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

    def test_merge_intervals(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], Array.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
        self.assertEqual([[1, 5]], Array.merge_intervals([[1, 4], [4, 5]]))
        self.assertEqual([[0, 4]], Array.merge_intervals([[1, 4], [0, 1]]))
        self.assertEqual([[2, 4], [5, 5]], Array.merge_intervals([[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]))

    def test_jump_game(self):
        self.assertEqual(True, Array.jump_game([2, 3, 1, 1, 4]))
        self.assertEqual(False, Array.jump_game([3, 2, 1, 0, 4]))
        self.assertEqual(True, Array.jump_game([2, 0]))
        self.assertEqual(True, Array.jump_game([2, 0, 0]))
        self.assertEqual(False, Array.jump_game([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1,
                                                 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0,
                                                 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0,
                                                 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2,
                                                 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]))
        with open('jump_game.json', 'r') as fr:
            from json import load
            data = load(fr)
            self.assertEqual(False, Array.jump_game(data))

    def test_container_with_most_water(self):
        self.assertEqual(49, Array.container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(16, Array.container_with_most_water([4, 3, 2, 1, 4]))
        self.assertEqual(1, Array.container_with_most_water([1, 1]))
        self.assertEqual(2, Array.container_with_most_water([1, 2, 1]))
        self.assertEqual(24, Array.container_with_most_water([1, 3, 2, 5, 25, 24, 5]))
        with open('container_with_most_water.json', 'r') as fr:
            from json import load
            self.assertEqual(48762645, Array.container_with_most_water(load(fr)))

    def test_count_number_of_nice_subarrays(self):
        self.assertEqual(2, Array.count_number_of_nice_subarrays(nums=[1, 1, 2, 1, 1], k=3))
        self.assertEqual(0, Array.count_number_of_nice_subarrays(nums=[2, 4, 6], k=1))
        self.assertEqual(16, Array.count_number_of_nice_subarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))
        self.assertEqual(3, Array.count_number_of_nice_subarrays(nums=[2044, 96397, 50143], k=1))

    def test_search_in_rotated_sorted_array(self):
        self.assertEqual(4, Array.search_in_rotated_sorted_array(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
        self.assertEqual(-1, Array.search_in_rotated_sorted_array(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
        self.assertEqual(-1, Array.search_in_rotated_sorted_array(nums=[1], target=0))
        self.assertEqual(-1, Array.search_in_rotated_sorted_array(nums=[1], target=2))
        self.assertEqual(1, Array.search_in_rotated_sorted_array(nums=[1, 3], target=3))

    def test_find_in_mountain_array(self):
        self.assertEqual(3, Array.find_in_mountain_array(2, Array.MountainArray([3, 5, 3, 2, 0])))
        self.assertEqual(2, Array.find_in_mountain_array(3, Array.MountainArray([1, 2, 3, 4, 5, 3, 1])))
        self.assertEqual(-1, Array.find_in_mountain_array(3, Array.MountainArray([0, 1, 2, 4, 2, 1])))
        self.assertEqual(2, Array.find_in_mountain_array(3, Array.MountainArray([1, 2, 3, 5, 3])))
        self.assertEqual(2, Array.find_in_mountain_array(2, Array.MountainArray([1, 5, 2])))
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 20, 19, 18, 17, 16, 15, 14,
                13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        self.assertEqual(-1, Array.find_in_mountain_array(22, Array.MountainArray(data)))
        data = list(range(0, 1000)) + list(range(999, 0, -2))
        self.assertEqual(500, Array.find_in_mountain_array(500, Array.MountainArray(data)))
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 100, 99, 98, 97,
                96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82]
        self.assertEqual(-1, Array.find_in_mountain_array(102, Array.MountainArray(data)))
        self.assertEqual(0, Array.find_in_mountain_array(1, Array.MountainArray([1, 5, 2])))

    def test_happy_number(self):
        self.assertEqual(True, Array.happy_number(19))
        self.assertEqual(False, Array.happy_number(2))

    def test_jump_game_ii(self):
        self.assertEqual(2, Array.jump_game_ii([2, 3, 1, 1, 4]))
        self.assertEqual(2, Array.jump_game_ii([2, 3, 0, 1, 4]))
        self.assertEqual(3, Array.jump_game_ii([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))
        self.assertEqual(0, Array.jump_game_ii([0]))
