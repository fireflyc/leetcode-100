import unittest

from leetcode.xs import DynamicProgramming


class DynamicProgrammingTestCase(unittest.TestCase):
    def test_house_robber(self):
        houses = [1, 2, 3, 1]
        self.assertEqual(4, DynamicProgramming.house_robber(houses))
        houses = [2, 7, 9, 3, 1]
        self.assertEqual(12, DynamicProgramming.house_robber(houses))

    def test_fib(self):
        self.assertEqual(1, DynamicProgramming.fib(2))
        self.assertEqual(2, DynamicProgramming.fib(3))
        self.assertEqual(55, DynamicProgramming.fib(10))

    def test_coin_change(self):
        self.assertEqual(3, DynamicProgramming.coin_change([1, 2, 5], 11))
        self.assertEqual(5, DynamicProgramming.coin_change([2, 3, 5, 7], 31))
        self.assertEqual(6, DynamicProgramming.coin_change([1, 2, 5, 7], 31))
        self.assertEqual(-1, DynamicProgramming.coin_change([2, 5, 7], 31))
        self.assertEqual(-1, DynamicProgramming.coin_change([2], 3))
        self.assertEqual(0, DynamicProgramming.coin_change([1], 0))
        self.assertEqual(100, DynamicProgramming.coin_change([1], 100))
