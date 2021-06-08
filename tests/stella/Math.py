import unittest
from leetcode.stella import Math


class MathTestCase(unittest.TestCase):
    def test_water_and_jug_problem(self):
        self.assertEqual(True, Math.water_and_jug_problem(3, 5, 4))
        self.assertEqual(False, Math.water_and_jug_problem(2, 6, 5))
