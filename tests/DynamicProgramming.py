import unittest

from dp import HouseRobber, Fibonacci, CoinChange


class DynamicProgrammingTestCase(unittest.TestCase):
    def test_house_robber(self):
        houses = [1, 2, 3, 1]
        self.assertEqual(4, HouseRobber.solution(houses))
        self.assertEqual(4, HouseRobber.rob(houses))
        houses = [2, 7, 9, 3, 1]
        self.assertEqual(12, HouseRobber.solution(houses))
        self.assertEqual(12, HouseRobber.rob(houses))

    def test_fib(self):
        self.assertEqual(1, Fibonacci.fib(2))
        self.assertEqual(2, Fibonacci.fib(3))
        self.assertEqual(55, Fibonacci.fib(10))

    def test_coin_change(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(3, CoinChange.coin_change(coins, amount))
