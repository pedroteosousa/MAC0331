from math import inf

epsilon = 1e-10

def nearly_equal(a, b):
    return abs(a-b) <= epsilon

class Point:
    "Um ponto de coordenadas (x,y)"

    def __init__ (self, x, y):
        "Cria um ponto a partir de suas coordenadas"
        self.x, self.y = x, y

    def __eq__ (self, p):
        "Verifica se dois pontos são iguais"
        return nearly_equal(self.x, p.x) and nearly_equal(self.y, p.y)

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

    def __repr__ (self):
        "Representação do ponto como uma string"
        return "Point" + str((self.x, self.y))

class Line:
    "Uma reta não vertical que obedece y=mx+b"

    @classmethod
    def cmp(self, x):
        "Retorna uma função que compara as retas no x dado"
        def cmp_x(l1, l2):
            t1, t2 = (0, 0), (0, 0)
            if x == inf:
                t1, t2 = (l1.m, l1.b), (l2.m, l2.b)
            elif x == -inf:
                t1, t2 = (-l1.m, l1.b), (-l2.m, l2.b)
            else:
                t1, t2 = (l1(x), -l1.m), (l2(x), -l2.m)
            return -1 if t1 < t2 else 0 if t1 == t2 else 1
        return cmp_x

    def __init__ (self, m, b):
        "Cria uma reta a partir de seus parâmetros"
        self.m, self.b = m, b

    def __eq__ (self, l):
        "Verifica se duas retas são iguais"
        return nearly_equal(self.m, l.m) and nearly_equal(self.b, l.b)

    def __contains__ (self, p):
        "Verifica se o ponto está contido na reta"
        return nearly_equal(p.y, self.m * p.x + self.b)

    def __call__ (self, x):
        "y da reta no ponto x"
        return self.m * x + self.b

    def __hash__ (self):
        "Hash da reta"
        return hash((self.m, self.b))

    def horizontal (self):
        "Verifica se a reta é horizontal"
        return nearly_equal(self.m, 0)

    def parallel (self, l):
        "Verifica se duas retas são paralelas"
        return nearly_equal(self.m, l.m)

    def perpendicular (self, l):
        "Verifica se duas retas são perpendiculares"
        if self.horizontal() or l.horizontal():
            return false
        return nearly_equal(-1.0, l.m * self.m)

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

    def __repr__ (self):
        "Representação da reta como uma string"
        return "Line" + str((self.m, self.b))

