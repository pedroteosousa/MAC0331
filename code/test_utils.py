import unittest
from basic import Line
from math import inf
import random
import utils

random.seed(0)

class TestUtils (unittest.TestCase):
    def test_count_intersections(self):
        l = [Line(7, 3), Line(-5, 9), Line(-1, 5), Line(-9, 60)]
        self.assertEqual(utils.intersections(l, (-inf, inf))[0], 6)
        self.assertEqual(utils.intersections(l, (0, 10))[0], 5)
        self.assertEqual(utils.intersections(l, (0, 2))[0], 3)
        self.assertEqual(utils.intersections(l, (3, inf))[0], 3)

    def test_random_inversion(self):
        l = [Line(7, 3), Line(-5, 9), Line(-1, 5), Line(-9, 60)]
        _, inv = utils.intersections(l, (-inf, inf))
        self.assertEqual(inv, (l[2], l[1]))
        _, inv = utils.intersections(l, (2, 3))
        self.assertEqual(inv, None)
        _, inv = utils.intersections(l, (3, 4))
        self.assertEqual(inv, (l[0], l[3]))

    def test_level(self):
        G = [Line(2, 7), Line(-1, -2), Line(-5, 0), Line(-1/5, 1), Line(-0.5, 3)]
        self.assertEqual(utils.level(G, 1, -10), Line(-0.2, 1));
        self.assertEqual(utils.level(G, 3, -2), Line(-1/2, 3));
        self.assertEqual(utils.level(G, 0, 0), Line(-1, -2));

if __name__ == "__main__":
	unittest.main()
