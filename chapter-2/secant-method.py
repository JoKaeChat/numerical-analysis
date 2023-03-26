import numpy as np

def secant(p0, p1, TOL, N0, f):
    i=2
    q0 = f(p0)
    q1 = f(p1)

    while i <= N0: 
        p = p1-q1*(p1-p0)/(q1-q0)

        print('{} iteration: p0 = {:.9f}\t p1 = {:.9f}\t    p = {:.9f} \t |p - p1| = {:.10f}'.format(i, p0, p1, p, np.abs(p - p0)))
        
        if np.abs(p - p0) < TOL:
            return p
        
        i = i+1

        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)

    print('The method failed after N0 iterations, N0 = {}'.format(N0))
    return p

f = lambda x: np.cos(x) - x
p0 = 0.5
p1 =  np.pi / 4
TOL = 1e-8
N0 = 7

p = secant(p0, p1, TOL, N0, f)