import unittest
from basic import Line
from math import inf
import random
import utils

class TestUtils (unittest.TestCase):
    def setUp(self):
        self.G1 = [Line(2, 7), Line(-1, -2), Line(-5, 0), Line(-0.2, 1), Line(-0.5, 3), Line(-5, 10), Line(0, 4)]
        self.G2 = [Line(4, -6), Line(-3, -5), Line(0, 5), Line(8, 9), Line(1, 6)]
        random.seed(0)

    def test_count_intersections(self):
        G = self.G1
        self.assertEqual(utils.intersections(G, (-inf, inf))[0], 20)
        self.assertEqual(utils.intersections(G, (0, 10))[0], 7)
        self.assertEqual(utils.intersections(G, (-1, 2))[0], 9)
        self.assertEqual(utils.intersections(G, (-3, inf))[0], 16)

    def test_random_inversion(self):
        G = self.G1
        inv = utils.intersections(G, (-inf, inf))[1]
        self.assertEqual(inv, (G[6], G[2]))
        inv = utils.intersections(G, (2, 3))[1]
        self.assertEqual(inv, None)
        inv = utils.intersections(G, (3, 4))[1]
        self.assertEqual(inv, (G[1], G[5]))

    def test_level(self):
        G = [Line(2, 7), Line(-1, -2), Line(-5, 0), Line(-0.2, 1), Line(-0.5, 3)]
        G = self.G1
        self.assertEqual(utils.level(G, 1, -10), G[3])
        self.assertEqual(utils.level(G, 2, -10), G[6])
        self.assertEqual(utils.level(G, 3, -2), G[6])
        self.assertEqual(utils.level(G, 6, 0), G[5])
        self.assertEqual(utils.level(G, 0, inf), G[2])
        self.assertEqual(utils.level(G, 0, -inf), G[0])

    def test_has_odd_intersections(self):
        G1, G2 = self.G1, self.G2
        p1, p2 = len(G1) // 2, len(G2) // 2
        self.assertTrue(utils.has_odd_intersections(G1, G2, p1, p2, (-inf, inf)))
        self.assertFalse(utils.has_odd_intersections(G1, G2, p1, p2, (-inf, -1)))
        self.assertTrue(utils.has_odd_intersections(G1, G2, p1, p2, (-1, inf)))
        self.assertFalse(utils.has_odd_intersections(G1, G2, p1, p2, (-3, -2)))
        self.assertTrue(utils.has_odd_intersections(G1, G2, p1, p2, (-1, 0)))
        self.assertFalse(utils.has_odd_intersections(G1, G2, p1, p2, (-1, -0.7)))
        self.assertTrue(utils.has_odd_intersections(G1, G2, p1, p2, (-0.7, 0.65)))

if __name__ == "__main__":
	unittest.main()
