import numpy as np
import matplotlib.pyplot as plt
import utils
import time
import random
import sys
from basic import Point, Line

def f(t):
    random.seed(0)
    start_time = time.time()

    bound = 2 ** 32
    rand_coord = lambda : random.randint(-bound, bound)
    P1, P2 = [], []
    for i in range(t):
        P1.append(Point(rand_coord(), rand_coord()))
        P2.append(Point(rand_coord(), rand_coord()))

    l = utils.ham_sandwich(P1, P2)
    print('Finished case with %d points' % (2 * t))
    return time.time() - start_time

plt.figure(1)

x = [(2 ** i) for i in range(15)]
y = [f(i) for i in x]

plt.plot(x, y, 'r--')
plt.show()
