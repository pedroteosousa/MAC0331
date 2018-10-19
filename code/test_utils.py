import unittest
from basic import Line
from math import inf
import utils

class TestUtils (unittest.TestCase):
    def test_count_intersections(self):
        l = [Line(7, 3), Line(-5, 9), Line(-1, 5), Line(-9, 60)]
        self.assertEqual(utils.count_intersections(l, (-inf, inf)), 6)
        self.assertEqual(utils.count_intersections(l, (0, 10)), 5)
        self.assertEqual(utils.count_intersections(l, (3, inf)), 3)

if __name__ == "__main__":
	unittest.main()
