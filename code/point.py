
from line import *

class Point:
	"Um ponto de coordenadas (x,y)"

	def __init__ (self, x, y):
		"Cria um ponto a partir de suas coordenadas"
		self.x, self.y = x, y

	def __eq__ (self, p):
		"Verifica se dois pontos são iguais"
		return (self.x, self.y) == (p.x, p.y)

	def dual (self):
		"Reta referente ao dual do ponto em questão"
		return Line(self.x, -self.y)

	def __contains__ (self, l):
		"Verifica se o ponto está contido na linha"
		return self.y == l.m * self.x + l.b 

	def above (self, l):
		"Verifica se o ponto está acima da reta"
		return self.y > l.m * self.x + l.b 

	def above_in (self, l):
		"Verifica se o ponto está acima ou na reta"
		return self.above(l) or self in l

	def under (self, l):
		"Verifica se o ponto está abaixo da reta"
		return not self.above_in(l);

	def under_in (self, l):
		"Verifica se o ponto está abaixo ou na reta"
		return not self.above(l);



