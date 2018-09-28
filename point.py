
from line import *

class Point:
	"Um ponto de coordenadas (x,y)"

	def __init__ (self, x, y):
		"Para criar um ponto, passe suas coordenadas"
		self.x, self.y = x, y

	def __eq__ (self, p):
		return (self.x, self.y) == (p.x, p.y)

	def dual (self):
		return Line(self.x, -self.y)

	def __contains__ (self, l):
		return self.y == l.m * self.x + l.b 

	def above (self, l):
		return self.y > l.m * self.x + l.b 

	def above_in (self, l):
		return self.above(l) or self in l

	def under (self, l):
		return not self.above_in(l);

	def under_in (self, l):
		return not self.above(l);



