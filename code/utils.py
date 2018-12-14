import functools
from basic import Line, Point
from random import randint

def intersections(G, T):
    "Número de intersecções e uma intersecção aleatória no intervalo T em O(n log n)"

    def inversions(v, p = 0):
        "Número de inversões e a p-ésima inversão de v"

        def merge(l, r, p):
            "Combina duas listas ordenadas, retorna numéro de inversões e a p-ésima inversão do merge"

            nv = []
            i, j, ni, inv = 0, 0, 0, None
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    nv.append(l[i])
                    i += 1
                else:
                    nv.append(r[j])
                    diff = len(l) - i
                    if ni < p and ni + diff >= p:
                        pos = p - ni
                        inv = (r[j], l[i + pos - 1])
                    ni += diff
                    j += 1
            nv += l[i:]
            nv += r[j:]
            return nv, ni, inv

        def sort(v, p):
            "Ordena uma lista v, retorna número de inversões e a p-ésima inversão de v"

            if len(v) <= 1:
                return v, 0, None
            mid = len(v) // 2
            l, ni_l, i_l = sort(v[:mid], p)
            r, ni_r, i_r = sort(v[mid:], p - ni_l)
            nv, ni_m, i_m = merge(l, r, p - ni_l - ni_r)
            return nv, ni_m + ni_l + ni_r, i_m or i_l or i_r
        
        v, ni, inv = sort(v, p)
        return ni, inv

    bijection = {}
    L = sorted(G, key=functools.cmp_to_key(Line.cmp(T[0])))
    R = sorted(G, key=functools.cmp_to_key(Line.cmp(T[1])))
    for i, l in enumerate(L):
        bijection[l] = i

    v = [bijection[l] for l in R]
    count, inv = inversions(v)
    v = [bijection[l] for l in R]
    count, inv = inversions(v, randint(1, max(1, count)))
    inv = inv if not inv else (L[inv[0]], L[inv[1]])
    return count, inv

def level(G, p, x):
    "p-ésimo elemento de G em x, se G estivesse ordenado"

    if len(G) == 1:
        return G[0]
    pivot = G[randint(0, len(G) - 1)]
    G_less = []
    G_greater = []

    for i in G:
        if Line.cmp(x)(i, pivot) < 0:
            G_less.append(i)
        elif Line.cmp(x)(i, pivot) > 0: 
            G_greater.append(i)

    if len(G_less) > p:
        return level(G_less, p, x)
    elif len(G) - len(G_greater) <=  p:
        return level(G_greater, p - (len(G) - len(G_greater)), x)
    else:
        return pivot

def has_odd_intersections(G1, G2, p1, p2, T):
    "verifica se a quantidade de intersecções entre os níveis p1 e p2 em T é ímpar"

    l, r = T
    left = Line.cmp(l)(level(G1, p1, l), level(G2, p2, l))
    right = Line.cmp(r)(level(G1, p1, r), level(G2, p2, r))
    return left * right < 0

def verify_solution(P1, P2, l):
    "verifica se a reta l resolve o problema para os conjuntos de pontos P1 e P2"

    if l is None:
        return False

    count = [[0, 0], [0, 0]]
    P = [P1, P2]
    for i in range(2):
        for p in P[i]:
            if p.above(l):
                count[i][0] += 1
            if p.under(l):
                count[i][1] += 1
        if 2 * max(count[i][0], count[i][1]) > len(P[i]):
            return False

    return True

def max_intersections(G):
    "conta a maior quantidade de intersecções possíveis no nível G"

    return (len(G) * (len(G) - 1)) // 2

def new_interval(G1, G2, p1, p2, T):
    "retorna um novo intervalo com a propriedade de intersecção ímpar e se a quantidade de retas é pequena o suficiente para um testa tudo"

    cur_intersections, random_inversion = intersections(G1, T)
    is_base = (max_intersections(G1) <= 32)
    while 32 * cur_intersections > max_intersections(G1) and not is_base:
        x = random_inversion[0].intersect(random_inversion[1]).x
        if has_odd_intersections(G1, G2, p1, p2, (T[0], x)):
            T = (T[0], x)
        else:
            T = (x, T[1])
        cur_intersections, random_inversion = intersections(G1, T)
    return T, is_base

def new_trapezoid(G, p, T):
    "retorna um trapezoide para eliminaçāo de retas"

    off = len(G) // 8
    dL1 = Point(T[0], level(G, p - off, T[0])(T[0]))
    dL2 = Point(T[0], level(G, p + off, T[0])(T[0]))
    dR1 = Point(T[1], level(G, p - off, T[1])(T[1]))
    dR2 = Point(T[1], level(G, p + off, T[1])(T[1]))
    return (dL1, dL2, dR2, dR1)

def intersects_trapezoid(l, t):
    "checa se a reta l intersecta o trapezoide t e se l está abaixo de t"

    is_under, is_above = True, True

    for i in range(4):
        if t[i].under_in(l):
            is_under = False

        if t[i].above_in(l):
            is_above = False
    
    return is_under, is_above

def discard_lines(G, p, t):
    nG = []
    b = 0
    for l in G:
        is_under, is_above = intersects_trapezoid(l, t)
        if not (is_under or is_above):
            nG.append(l)
        elif is_under:
            b += 1
    return nG, p - b

