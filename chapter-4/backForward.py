import numpy as np

def finite_difference(f,a,h):
    val = (f(h+a) - f(a))/h
    return val

f = lambda x: np.log(x)
a = 1.8
h_val = [0.1, 0.05, 0.01]
for h in h_val:
    val = finite_difference(f,a,h)
    print('the forward-difference: {}\t error: {}'.format(val, np.abs(5/9 - val)))