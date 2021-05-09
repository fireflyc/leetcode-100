import unittest

from leetcode.stella import DynamicProgramming


class DynamicProgrammingTestCase(unittest.TestCase):
    def test_house_robber(self):
        self.assertEqual(4, DynamicProgramming.house_robber([1, 2, 3, 1]))
        self.assertEqual(22, DynamicProgramming.house_robber([2, 1, 9, 20, 1]))
        self.assertEqual(10, DynamicProgramming.house_robber([2, 1, 1, 7, 1, 1]))

    def test_coin_change(self):
        self.assertEqual(3, DynamicProgramming.coin_change([1, 2, 5], 11))
        self.assertEqual(5, DynamicProgramming.coin_change([2, 3, 5, 7], 31))
        self.assertEqual(6, DynamicProgramming.coin_change([1, 2, 5, 7], 31))
        self.assertEqual(-1, DynamicProgramming.coin_change([2, 5, 7], 31))
        self.assertEqual(-1, DynamicProgramming.coin_change([2], 3))
        self.assertEqual(0, DynamicProgramming.coin_change([1], 0))
        self.assertEqual(100, DynamicProgramming.coin_change([1], 100))

    def test_coin_change2(self):
        self.assertEqual(4, DynamicProgramming.coin_change2([1, 2, 5], 5))
        self.assertEqual(1, DynamicProgramming.coin_change2([7], 0))
        self.assertEqual(35502874, DynamicProgramming.coin_change2([3, 5, 7, 8, 9, 10, 11], 500))

    def test_length_of_lts(self):
        self.assertEqual(4, DynamicProgramming.length_of_lts([10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(3, DynamicProgramming.length_of_lts([4, 10, 4, 3, 8, 9]))
        self.assertEqual(4, DynamicProgramming.length_of_lts([0, 1, 0, 3, 2, 3]))
        self.assertEqual(6, DynamicProgramming.length_of_lts([1, 3, 6, 7, 9, 4, 10, 5, 6]))
        self.assertEqual(2500, DynamicProgramming.length_of_lts(list(range(1, 2501))))

    def test_min_cost_tickets(self):
        self.assertEqual(11, DynamicProgramming.min_cost_tickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
        self.assertEqual(6, DynamicProgramming.min_cost_tickets([1, 4, 6, 7, 8, 20], [7, 2, 15]))
        self.assertEqual(423, DynamicProgramming.min_cost_tickets([
            1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30,
            31, 34, 37, 38, 39, 41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76,
            78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99
        ], [9, 38, 134]))

    def test_unique_binary_search_trees(self):
        self.assertEqual(5, DynamicProgramming.unique_binary_search_trees(3))
        self.assertEqual(1, DynamicProgramming.unique_binary_search_trees(19))

    def test_trapping_rain_water(self):
        self.assertEqual(6, DynamicProgramming.trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(9, DynamicProgramming.trapping_rain_water([4, 2, 0, 3, 2, 5]))
