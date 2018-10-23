import functools
from basic import Line
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
    elif  len(G) - len(G_greater) <=  p:
        return level(G_greater, p - (len(G) - len(G_greater)), x)
    else:
        return pivot
