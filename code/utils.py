import functools
from basic import Line

def count_intersections(G, T):
    "Número de intersecções no intervalo T em O(n log n)"

    def inversions(v):
        "Número de inversões em v"

        def merge(l, r):
            "Combina duas listas ordenadas e conta as inversões"

            nv = []
            i, j, inv = 0, 0, 0
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    nv.append(l[i])
                    i += 1
                else:
                    nv.append(r[j])
                    j += 1
                    inv += len(l) - i
            nv += l[i:]
            nv += r[j:]
            return nv, inv
        
        def sort(v):
            "Ordena uma lista v e conta suas inversões"
            
            if len(v) <= 1:
                return v, 0
            mid = len(v) // 2
            l, il = sort(v[:mid])
            r, ir = sort(v[mid:])
            nv, inv = merge(l, r)
            return nv, inv + il + ir
        
        v, inv = sort(v)
        return inv
    
    bijection = {}
    L = sorted(G, key=functools.cmp_to_key(Line.cmp(T[0])))
    for i, l in enumerate(L):
        bijection[l] = i
    v = [bijection[l] for l in sorted(G, key=functools.cmp_to_key(Line.cmp(T[1])))]
    return inversions(v)
