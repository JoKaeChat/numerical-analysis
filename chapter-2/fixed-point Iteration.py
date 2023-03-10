import numpy as np


def fixed_point(p0, TOL, NO, g):
    i = 1
    while (i <= NO):

        p = g(p0)
        print("{} iteration : p = {} ".format(i, p))
        if np.abs(p-p0) < TOL:
            return p
        i = i+1
        p0 = p

    print("The method failed after NO iterations, No = {}", format(NO))
    return p


def g(x): return x - x**3 - 4*x**2 + 10


p0 = 1.5
TOL = 1e-9
NO = 50
print("{} iteration : p = {} ".format(0, p0))
ans = fixed_point(p0, TOL, NO, g)
print(ans)
