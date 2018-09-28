
from point import *

class Line:
	"Uma reta não vertical que obedece y=mx+b"

	def __init__ (self, m, b):
		"Cria uma reta a partir de seus parâmetros"
		self.m, self.b = m, b

	def __eq__ (self, l):
		"Verifica se duas retas são iguais"
		return (self.m, self.b) == (l.m, l.b)

	def dual (self):
		"Ponto referente ao dual da reta em questão"
		return Point(self.m, -self.b)

	def horizontal (self):
		"Verifica se a reta é horizontal"
		return self.m == 0

	def parallel (self, l):
		"Verifica se duas retas são paralelas"
		return self.m == l.m

	def perpendicular (self, l):
		"Verifica se duas retas são perpendiculares"
		if self.horizontal() or l.horizontal():
			return false
		return -1.0/self.m == l.m

	def intersect (self, l):
		"Intersecção de duas retas (pode ser nada, um ponto ou uma reta)"
		if self == l:
			return Line(self.m, self.b)
		if self.parallel(l):
			return None
		x = -(self.b - l.b) / (self.m - l.m)
		y = self.m * x + self.b
		return Point(x, y)

