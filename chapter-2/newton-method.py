import numpy as np
import math

def newton(p0, TOL, N0, f, fp):
    i=1

    while i <= N0: #Step 2
        p=p0-f(p0)/fp(p0)

        print('{} iteration: p0 = {:.7f}\t p = {:.7f} \t    |p - p0| = {:.8f}'.format(i, p0, p, np.abs(p - p0)))
        
        if np.abs(p - p0) < TOL:
            return p
       
        i = i+1

        p0 = p

    print('The method failed after N0 iterations, N0 = {}'.format(N0))
    return p

f = lambda x: -x**3-math.cos(x)
fp = lambda x: -3*x**2+math.sin(x)
p0 = 0
N0 = 3
TOL = 1e-8




p = newton(p0,TOL,N0,f,fp)