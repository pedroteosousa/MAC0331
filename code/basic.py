class Point:
	"Um ponto de coordenadas (x,y)"

	def __init__ (self, x, y):
		"Cria um ponto a partir de suas coordenadas"
		self.x, self.y = x, y

	def __eq__ (self, p):
		"Verifica se dois pontos são iguais"
		return (self.x, self.y) == (p.x, p.y)

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

	def dual (self):
		"Reta referente ao dual do ponto em questão"
		return Line(self.x, -self.y)

class Line:
	"Uma reta não vertical que obedece y=mx+b"

	def __init__ (self, m, b):
		"Cria uma reta a partir de seus parâmetros"
		self.m, self.b = m, b

	def __eq__ (self, l):
		"Verifica se duas retas são iguais"
		return (self.m, self.b) == (l.m, l.b)

	def __contains__ (self, p):
		"Verifica se o ponto está contido na reta"
		return p.y == self.m * p.x + self.b 

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

	def dual (self):
		"Ponto referente ao dual da reta em questão"
		return Point(self.m, -self.b)

