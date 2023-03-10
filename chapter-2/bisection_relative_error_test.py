import numpy as np


def bisection_relative_error_test(a, b, TOL, N0, f):
    # Step 1
    i = 1
    FA = f(a)
    p_old = a
    print('iter \t    a_n\t      b_n\t p_n   f(a_n)  f(p_n)  RelErr')
    while i <= N0:  # Step 2
        # Step 3
        p = (a+b)/2
        FP = f(p)
        RelErr = np.abs(p - p_old)/np.abs(p)

        print('{}\t {:.6f}  {:.6f}  {:.6f}  {:>5.3f}  {:>+5.3f}  {:.5f}'.format(i,
              a, b, p, FA, FP, RelErr))
        # Step 4
        if FP == 0 or (b-a)/2 < TOL:
            return p
        # Step 5
        i = i+1
        # Step 6
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    print('Method failed after N0 iterations, N0 = {}'.format(N0))
    return p


def f(x): return x**3 + 4*x**2 - 10


a = 1
b = 2
N0 = 20
TOL = 1e-4
p = bisection_relative_error_test(a, b, TOL, N0, f)
