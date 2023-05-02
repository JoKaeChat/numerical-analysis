import numpy as np

def natural_cubic_spline(n,x,fval):
    a = fval
    b = np.zeros(n)
    c = np.zeros(n+1)
    d = np.zeros(n)
    h = np.zeros(n)
    l = np.zeros(n+1)
    mu = np.zeros(n)
    z = np.zeros(n+1)
    alpha = np.zeros(n)
    # Step 1
    for i in range(n):
        h[i] = x[i+1] - x[i]
    # Step 2
    for i in range(1,n):
        alpha[i] = (3/h[i])*(a[i+1]-a[i]) - (3/h[i-1])*(a[i]-a[i-1])
    # Step 3
        l[0] = 1
        mu[0] = 0
        z[0] = 0
    # Step 4
    for i in range(1,n):
        l[i] = 2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i]-h[i-1]*z[i-1])/l[i]

    # Step 5
        l[n] = 1
        z[n] = 0
        c[n] = 0        
    # Step 6
    for j in reversed(range(n)):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (a[j+1]-a[j])/(h[j]-h[j]*(c[j+1]+2*c[j]))/3
        d[j] = (c[j+1]-c[j])/(3*h[j])
    return (a,b,c,d)

n = 2
x = np.array([0,1,2])
fval = x    

a,b,c,d = natural_cubic_spline(n,x,fval)
print('a = \n', a)
print('b = \n', b)
print('c = \n', c)
print('d = \n', d)