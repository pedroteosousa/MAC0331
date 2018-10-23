# MAC0331
[![Build Status](https://travis-ci.org/pedroteosousa/MAC0331.svg?branch=master)](https://travis-ci.org/pedroteosousa/MAC0331)

Trabalho de Geometria Computacional

Rode `git submodule update --init --recursive` para baixar o repositório `geocomp-py-framework`

##### Links relevantes
- [Página dos projetos no site da Cris](https://www.ime.usp.br/~cris/aulas/18_2_331/projetos.html)
- [Paper sobre o algoritmo](https://link.springer.com/content/pdf/10.1007%2FBF02574017.pdf)

##### Pseudo Código

```python
# conta a quantidade de intersecções de G no intervalo T
def countIntersections(G, T):
   return countInversions(G(T.l), G(T.r))

# retorna a p-ésima reta de G no ponto x
def level(G, p, x):
    return G.sorted(x)[p]

# verifica se um intervalo T possui uma quantidade ímpar
# de intersecções entre os níveis p1 e p2
def hasOddIntersections(G1, G2, p1, p2, T):
    l, r = T
    sigL1, sigL2 = level(G1, p1, l)(l), level(G2, p2, l)(l)
    sigR1, sigR2 = level(G1, p1, r)(r), level(G2, p2, r)(r)
    return (sigL1 - sigL2) * (sigR1 - sigR2) < 0

# calcula o novo intervalo de busca
def newInterval(G1, G2, p1, p2, T):
    it = countIntersections(G1, T)
    while 32 * countIntersections(G1, T) > it:
        if hasOddIntersections(G1, G2, p1, p2, (T.l, T.mid)):
            T.r = T.mid
        else:
            T.l = T.mid
    return T

# constroi um trapezoide no intervalo T
def trapezoid(G, p, T):
    off = |G| / 8
    dL1 = level(G, p - off, l)(l)
    dL2 = level(G, p + off, l)(l)
    dR1 = level(G, p - off, r)(r)
    dR2 = level(G, p + off, r)(r)
    return (dL1, dL2, dR2, dR1)

# remove todas as retas que não intersectam t
# e calcula o novo nível p
def discardLines(G, p, t):
    nG = []
    b = 0
    for line in G:
        if line.intersects(t):
            nG += line
        elif line.isUnder(t):
                b += 1
    return nG, p - b

# retorna a intersecção da p1-ésima reta de G1 com a
# p2-ésima reta de G2 no intervalo T = (l, r)
def hamSandwich(G1, G2, p1, p2, T):
    if |G1| == |G2| == 1:
        return G1[p1].intersection(G2[p2])
    if |G1| < |G2|:
        return hamSandwich(G2, G1, p2, p1, T)
    T = newInterval(G1, G2, p1, p2, T)
    t = trapezoid(G1, p1, T)
    G1, p1 = dicardLines(G1, p1, t)
    G2, p2 = dicardLines(G2, p2, t)
    return hamSandwich(G1, G2, p1, p2, T)
```
