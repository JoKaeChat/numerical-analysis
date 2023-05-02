def simpson(f,a,b,c,h) :
    ans = h*(f(a)+4*f(b)+f(c))/3
    return ans



f = lambda x : x**4
a = 0.5
c= 1
b = (a+c)/2
h = b-a/2
print(simpson(f,a,b,c,h))