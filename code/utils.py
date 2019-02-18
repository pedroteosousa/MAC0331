import functools
from .basic import Point, Line
from random import randint, seed
from math import inf

from geocomp.common import control
from geocomp.common.guiprim import *

def intersections(G, T):
    "Número de intersecções e uma intersecção aleatória no intervalo T em O(n log n)"

    def inversions(v, p = 0):
        "Número de inversões e a p-ésima inversão de v"

        def merge(l, r, p):
            "Combina duas listas ordenadas, retorna numéro de inversões e a p-ésima inversão do merge"

            ll, rl = l
            lr, rr = r
            n, nv = 0, [0] * (rr + rl - lr - ll + 2)
            i, j, ni, inv = ll, lr, 0, None
            while i <= rl and j <= rr:
                if v[i] <= v[j]:
                    nv[n] = v[i]
                    n += 1
                    i += 1
                else:
                    nv[n] = v[j]
                    n += 1
                    diff = (rl - ll + 1) - (i - ll)
                    if ni < p and ni + diff >= p:
                        pos = p - ni
                        inv = (v[j], v[i + pos - 1])
                    ni += diff
                    j += 1
            while i <= rl:
                nv[n] = v[i]
                n += 1
                i += 1
            while j <= rr:
                nv[n] = v[j]
                n += 1
                j += 1
            for i in range(ll, rr + 1):
                v[i] = nv[i - ll]
            return ni, inv

        def sort(t, p):
            "Ordena uma lista v, retorna número de inversões e a p-ésima inversão de v"

            l, r = t
            if r - l + 1 <= 1:
                return 0, None
            mid = (l + r + 1) // 2
            ni_l, i_l = sort((l, mid - 1), p)
            ni_r, i_r = sort((mid, r), p - ni_l)
            ni_m, i_m = merge((l, mid - 1), (mid, r), p - ni_l - ni_r)
            return ni_m + ni_l + ni_r, i_m or i_l or i_r
        
        ni, inv = sort((0, len(v) - 1), p)
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

    return sorted(G, key=functools.cmp_to_key(Line.cmp(x)))[p]

def has_odd_intersections(G1, G2, p1, p2, T):
    "verifica se a quantidade de intersecções entre os níveis p1 e p2 em T é ímpar"

    l, r = T
    left = Line.cmp(l)(level(G1, p1, l), level(G2, p2, l))
    right = Line.cmp(r)(level(G1, p1, r), level(G2, p2, r))
    return left * right < 0

def verify_solution(P1, P2, l):
    "verifica se a reta l resolve o problema para os conjuntos de pontos P1 e P2"

    count = [[0, 0], [0, 0]]
    P = [P1, P2]
    for i in range(2):
        for p in P[i]:
            if p in l:
                continue
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

    ids = [None, None]

    def draw_interval(should_plot = True):
        control.thaw_update()
        for i in range(2):
            if not ids[i] == None:
                control.plot_delete(ids[i])
            if T[i] != -inf and T[i] != +inf and should_plot:
                ids[i] = control.plot_vert_line(T[i], 'yellow')
        control.sleep()
        control.freeze_update()

    cur_intersections, random_inversion = intersections(G1, T)
    is_base = (max_intersections(G1) <= 32)
    while 32 * cur_intersections > max_intersections(G1) and not is_base:
        x = random_inversion[0].intersect(random_inversion[1]).x
        if has_odd_intersections(G1, G2, p1, p2, (T[0], x)):
            T = (T[0], x)
        else:
            T = (x, T[1])
        cur_intersections, random_inversion = intersections(G1, T)
        draw_interval()
    draw_interval(False)
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
        control.freeze_update()
        new_plot_id = control.plot_line(0, l(0), 1, l(1), 'cyan')
        control.sleep()
        control.thaw_update()
        control.freeze_update()
        is_under, is_above = intersects_trapezoid(l, t)
        if not (is_under or is_above):
            nG.append(l)
        elif is_under:
            b += 1
        if (is_under or is_above):
            delete_lines([l])
        control.plot_delete(new_plot_id)
        control.sleep()
        control.thaw_update()

    return nG, p - b

def recursive_ham_sandwich(G1, G2, p1, p2, T):
    if len(G1) < len(G2):
        return recursive_ham_sandwich(G2, G1, p2, p1, T)
    T, is_base = new_interval(G1, G2, p1, p2, T)

    if is_base:
        valid_answers = []
        for g in G1:
            for h in G2:
                p = g.intersect(h)
                if p and isinstance(p.dual(), Line):
                    valid_answers.append(p.dual())
        delete_lines(G1+G2)
        return valid_answers

    t = new_trapezoid(G1, p1, T)
    t_ids = []
    control.freeze_update()
    for i in range(4):
        j = (i + 1) % 4
        t_ids.append(control.plot_segment(t[i].x, t[i].y, t[j].x, t[j].y, 'yellow'))
    control.sleep()
    control.thaw_update()

    G1, p1 = discard_lines(G1, p1, t)
    G2, p2 = discard_lines(G2, p2, t)

    for id in t_ids:
        control.plot_delete(id)

    return recursive_ham_sandwich(G1, G2, p1, p2, T)

def ham_sandwich(P1, P2):
    G1 = points_to_lines(P1, 'red')
    G2 = points_to_lines(P2, 'blue')
    valid_answers = recursive_ham_sandwich(G1, G2, len(G1)//2, len(G2)//2, (-inf, inf))
    for l in valid_answers:
        if verify_solution(P1, P2, l):
            return l
    return None

def points_to_lines(P, color):
    G = []
    for p in P:
        control.thaw_update()
        p.tk.hilight(color)
        control.sleep()
        control.freeze_update()
        g = p.dual()
        g.plot_id = control.plot_line(0, g(0), 1, g(1), color)
        G.append(g)
        p.tk.unhilight()
        p.tk.unplot()
        control.sleep()
    return G

def delete_lines(G):
    control.freeze_update()
    for g in G:
        control.plot_delete(g.plot_id)
    control.sleep()
    control.thaw_update()

def plot_points(P, color):
    control.freeze_update()
    for p in P:
        p.tk.hilight(color)
    control.sleep()
    control.thaw_update()

def partition_and_run(p):
    seed(0)
    P = [Point.from_framework_point(i) for i in p]

    half = len(P) // 2
    P1, P2 = P[:half+1], P[half+1:]

    line = ham_sandwich(P1, P2)
    plot_points(P1,'red')
    plot_points(P2,'blue')
    control.plot_line(0, line(0), 100000, line(100000), 'green')
