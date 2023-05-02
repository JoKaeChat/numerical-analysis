import numpy as np

def clamped_cubic_spline(n,x,fval,FPO,FPN):
    a = fval
    b = np.zeros(n)
    c = np.zeros(n+1)
    d = np.zeros(n)
    h = np.zeros(n)
    l = np.zeros(n+1)
    mu = np.zeros(n)
    z = np.zeros(n+1)
    alpha = np.zeros(n+1)
    # Step 1
    for i in range(n):
        h[i] = x[i+1]-x[i]
    # Step 2
        alpha[0] = 3*(a[1]-a[0])/h[0] -3*FPO
        alpha[n] = 3*FPN -3*(a[n]-a[n-1])/h[n-1]
    # Step 3
    for i in range(1,n):
        alpha[i] = (3/h[i])*(a[i+1]-a[i])-(3/h[i-1])*(a[i]-a[i-1])
    # Step 4
        l[0] = 2*h[0]; mu[0] =0.5; z[0] = alpha[0]/l[0]
    # Step 5
    for i in range(1,n):
        l[i] = 2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i]-h[i-1]*z[i-1])/l[i]
    # Step 6
        l[n] = h[n-1]*(2-mu[n-1])
        z[n] = (alpha[n]-h[n-1]*z[n-1])/l[n]
        c[n] = z[n]
    # Step 7
    for j in reversed(range(n)):
        c[j] = z[j]-mu[j]*c[j+1]
        b[j] = (a[j+1]-a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1]-c[j])/(3*h[j])
    return (a,b,c,d)

n = 3
x = np.array([0,1,2,3])
fval = x
FPO = 1
FPN = 1  

a,b,c,d = clamped_cubic_spline(n,x,fval,FPO,FPN)
print('a = \n', a)
print('b = \n', b)
print('c = \n', c)
print('d = \n', d)