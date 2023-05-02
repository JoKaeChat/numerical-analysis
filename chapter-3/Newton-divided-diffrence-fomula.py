import numpy as np

def newton_divided_difference(x,fval):
    n = x.shape[0]
    F = np.zeros((n,n))
    F[:,0] = fval
    # Step 1
    for i in range(1,n):
        for j in range(1,i+1):
            F[i,j] = ( F[i,j-1] - F[i-1,j-1]) / (x[i] - x[i-j])
    return np.diag(F)

x = np.array([-0.1, 0.0, 0.2, 0.3,0.35])
fval = np.array([5.30000,2.00000,3.19000,1.00000,0.97260])


coef = newton_divided_difference(x,fval)
print(coef)  


# ## P(n) 계산을 빠르게 ( nested form )
# def newton_interpolation(t,x,coef):
#     n = len(coef)
#     val = coef[n-1]
#     for i in reversed(range(n-1)):
#         val *= (t-x[i])
#         val += coef[i]
#     return val

# t = 1.5
# val = newton_interpolation(t,x,coef)
# print(val)