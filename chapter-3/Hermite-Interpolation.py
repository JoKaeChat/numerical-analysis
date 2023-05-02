import numpy as np
import math

def hermite_coef(x,fval,dfval):
    n = len(x)
    z = np.zeros(2*n)
    Q = np.zeros((2*n,2*n))
    # Step 1
    for i in range(n):
        # Step 2
        z[2*i] = x[i]
        z[2*i+1] = x[i]
        Q[2*i,0] = fval[i]
        Q[2*i+1,0] = fval[i]
        Q[2*i+1,1] = dfval[i]
        
        # Step 3
        if i != 0:
            Q[2*i, 1] = (Q[2*i,0] -Q[2*i-1,0])/(z[2*i] -z[2*i-1])
    
    # Step 4
    for i in range(2,2*n):
        for j in range(2,i+1):
            Q[i,j] = (Q[i,j-1]-Q[i-1,j-1])/(z[i] - z[i-j])
    return (np.diag(Q), z)

x = np.array([0,0.5])
fval = np.array([1,2.71828])
dfval = np.array([2,5.43656])

coef, z = hermite_coef(x,fval,dfval)
print(coef)
print(z)


# def hermite_interpolation(t,z,coef):
#     n = len(coef)
#     val = coef[n-1]
#     for i in reversed(range(n-1)):
#         val *= (t-z[i])
#         val += coef[i]
#     return val

# t = 0.45
# val = hermite_interpolation(t,z,coef)
# print(val)

