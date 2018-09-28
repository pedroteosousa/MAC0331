
from point import *

class Line:
	"Uma reta não vertical que obedece y=mx+b"

	def __init__ (self, m, b):
		"Para criar uma reta, passe seus parâmetros"
		self.m, self.b = m, b

	def __eq__ (self, l):
		return (self.m, self.b) == (l.m, l.b)

	def dual (self):
		return Point(self.m, -self.b)

	def horizontal (self):
		return self.m == 0

	def parallel (self, l):
		return self.m == l.m

	def perp (self, l):
		if self.horizontal() or l.horizontal():
			return false
		return -1.0/self.m == l.m

	def intersect (self, l):
		if self == l:
			return Line(self.m, self.b)
		if self.parallel(l):
			return None
		x = -(self.b - l.b) / (self.m - l.m)
		y = self.m * x + self.b
		return Point(x, y)

