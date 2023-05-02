import numpy as np
import math


def Lagrange_polynomial(t,x,fval):
    n = x.shape[0]
    L = np.ones(n)
    for i in range(0,n):
        for j in range(0,n):
            if i!=j:
                L[i] *= (t-x[j])/(x[j]-x[i])
    val = np.sum(L*fval)
    return val 

x = np.array([0, 0.6])
fval = math.cos(x)
t = 3
val = Lagrange_polynomial(t,x,fval)
print(val)    