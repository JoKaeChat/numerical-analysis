def trapezoidal(f,a,b,h) :
    ans = h*(f(a)+f(b))/2
    return ans



f = lambda x : x**4
a = 0.5
b = 1
h = b-a
print(trapezoidal(f,a,b,h))
