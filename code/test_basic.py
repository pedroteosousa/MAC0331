import unittest
from basic import Point, Line

class TestPoint (unittest.TestCase):

	def test_init (self):
		p = Point(-20.5, 25)
		self.assertEqual((p.x, p.y), (-20.5, 25))
		q = Point(0, 0)
		self.assertEqual((q.x, q.y), (0, 0))
		r = Point(135,-135)
		self.assertEqual((r.x, r.y), (135, -135))

	def test_eq (self):
		a = Point(1, 10)
		b = Point(1, 10)
		c = Point(0, 0)
		self.assertEqual(a, b)
		self.assertNotEqual(a, c)
		self.assertNotEqual(b, c)

	def test_above (self):
		a = Point(10, 10)
		b = Point(12, 13)

	def test_dual (self):
		a = Point(0, 0)
		self.assertEqual(a.dual(), Line(0, 0))
		b = Point(0, -1)
		self.assertEqual(b.dual(), Line(0, 1))
		c = Point(-1, 2)
		self.assertEqual(c.dual(), Line(-1, -2))
		d = Point(-0.5,-2)
		self.assertEqual(d.dual(), Line(-0.5, 2))

class TestLine (unittest.TestCase):

	def test_contains (self):
		a = Point(1, 1)
		b = Point(-12, -12)
		c = Point(27, -12)
		x = Line(1, 0)
		y = Line(-1, 2)
		z = Line(0, -12)
		self.assertTrue (a in x)
		self.assertTrue (a in y)
		self.assertFalse(a in z)
		self.assertTrue (b in x)
		self.assertFalse(b in y)
		self.assertTrue (b in z)
		self.assertFalse(c in x)
		self.assertFalse(c in y)
		self.assertTrue (c in z)


	

