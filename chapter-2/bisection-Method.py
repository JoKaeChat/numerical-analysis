import math


def bisection(a, b, TOL, NO, f):
    i = 1
    FA = f(a)

    while i <= NO:
        p = (a+b)/2
        FP = f(p)

        if FP == 0 or (b-a)/2 < TOL:
            return p
        i = i+1

        if FA*FP > 0:
            a = p
        else:
            b = p

    print("Method failed after NO iterations, NO ={}", format(NO))
    return p


def f(x): return x**(1/2)-math.cos(x)


a = 0
b = 1
NO = 3
TOL = 1e-4

p = bisection(a, b, TOL, NO, f)
print(p)
