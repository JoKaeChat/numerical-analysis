import numpy as np

def composite_simpson(f,a,b,n):
    # Step 1
    h = (b-a)/n
    # Step 2
    XI0 = f(a) + f(b)
    XI1 = 0
    XI2 = 0
    # Step 3
    for i in range(1,n):
        # Step 4
        X = a+i*h
        # Step 5
        if i%2 == 0:
            XI2 += f(X)
        else:
            XI1 +=  f(X)
    # Step 6
    XI = h*(XI0+2*XI2+4*XI1)/3
    return XI

f = lambda x: np.sin(x)
nI = [4,8,12,16,20]
a = 0
b = np.pi
I = 2
for n in nI:
    XI = composite_simpson(f,a,b,n)
    print("Composite Simpson's Rule: {}\t error: {}".format(XI, np.abs(XI - I)))