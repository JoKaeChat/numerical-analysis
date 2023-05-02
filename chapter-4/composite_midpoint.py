import numpy as np

def composite_midpoint(f,a,b,n):
    h = (b-a)/(n+2)
    XI = 0
    for i in range(0,n//2):
        X = a+(2*i+1)*h
        XI += f(X)
    XI *= 2*h
    return XI

f = lambda x: np.sin(x)
nI = [40,80,120,160,200]
a = 0
b = np.pi
I = 2
for n in nI:
    XI = composite_midpoint(f,a,b,n)
    print("Composite Midpoint Rule: {}\t error: {}".format(XI, np.abs(XI - I)))