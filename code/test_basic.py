import unittest
from basic import Point, Line
from math import inf

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
	def test_cmp (self):
		l = Line(3, 5)
		g = Line(-4, 2)
		# x = -inf
		self.assertLess(Line.cmp(-inf)(l, g), 0)
		self.assertGreater(Line.cmp(-inf)(g, l), 0)
		# x = -3/7
		self.assertEqual(Line.cmp(-3/7)(l, g), 0)
		self.assertEqual(Line.cmp(-3/7)(g, l), 0)
		# x = 7
		self.assertGreater(Line.cmp(7)(l, g), 0)
		self.assertLess(Line.cmp(7)(g, l), 0)
		# x = +inf
		self.assertGreater(Line.cmp(inf)(l, g), 0)
		self.assertLess(Line.cmp(inf)(g, l), 0)

	def test_init (self):
		val = (5.5, -5)
		l = Line(*val)
		self.assertEqual((l.m, l.b), val)
	
	def test_eq (self):
		l = Line (-5, 9)
		g = Line (-5, 9)
		h = Line (-5, -9)
		self.assertEqual(l, g)
		self.assertNotEqual(l, h)
	
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

	def test_call (self):
		l = Line(5, 1/3)
		self.assertAlmostEqual(l(2), 31/3)
		self.assertAlmostEqual(l(0), 1/3)
	
	def test_hash (self):
		l = Line(-9, 1/3)
		self.assertEqual(hash(l), hash((l.m, l.b)))
	
	def test_horizontal (self):
		l = Line(0, -8)
		g = Line(0.00001, -5)
		self.assertTrue(l.horizontal())
		self.assertFalse(g.horizontal())
	
	def test_parallel (self):
		l = Line(5, 10)
		g = Line(5, -125)
		self.assertTrue(l.parallel(g))
		self.assertTrue(g.parallel(l))

		# horizontal lines
		l = Line (0, 0)
		g = Line (0, -5)
		self.assertTrue(l.parallel(g))
	
	def test_perpendicular (self):
		l = Line(.5, 10)
		g = Line(-2, 550)
		h = Line(1, 5)
		self.assertTrue(l.perpendicular(g))
		self.assertTrue(g.perpendicular(l))
		self.assertFalse(l.perpendicular(h))

	def test_intersect (self):
		# None
		l = Line(5, 10)
		g = Line(5, -125)
		self.assertEqual(l.intersect(g), None)	

		# Point
		l = Line(6, 8)
		g = Line(-1, -3)
		self.assertEqual(l.intersect(g), Point(-11.0/7.0, -10.0/7.0))

		# Line
		l = Line(10, -1/3)
		g = Line(10, -1/3)
		self.assertEqual(l.intersect(g), l)

	def test_dual (self):
		l = Line(3.3, 8)
		p = Point(3.3, -8)
		self.assertEqual(l.dual(), p)

if __name__ == "__main__":
	unittest.main()
