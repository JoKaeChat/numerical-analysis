import numpy as np

def composite_trapezoid(f,a,b,n):
    h = (b-a)/n
    XI0 = f(a)+f(b)
    XI1 = 0
    for i in range(1,n):
        X = a + i*h
        XI1 += f(X)
    XI = h*(XI0+2*XI1)/2
    return XI

f = lambda x: np.sin(x)
nI = [20,40,60,80,100]
a = 0
b = np.pi
I = 2
for n in nI:
    XI = composite_trapezoid(f,a,b,n)
    print("Composite Trapezoidal Rule: {}\t error: {}".format(XI, np.abs(XI - I)))
