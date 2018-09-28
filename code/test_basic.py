import unittest
from basic import Point

class TestPoint (unittest.TestCase):

	def test_eq (self):
		a = Point(1, 10)
		b = Point(1, 10)
		c = Point(0, 0)
		self.assertEqual(a, b)
		self.assertNotEqual(a, c)
		self.assertNotEqual(b, c)

	

