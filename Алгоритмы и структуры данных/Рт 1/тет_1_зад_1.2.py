# точность 0.0001
import math

def f(x):
    return (math.acos(x) - math.sqrt(1 - 0.3 * x ** 3))

R = 1
L = 0
if f(R) > f(L):
    while f(L) > 0.0001:
        L = L - (((R - L) * (f(L))) / (f(R) - f(L)))
    print(L)
    print(f(L))

else:
    while abs(f(R)) > 0.0001:
        R = R - (((L - R) * (f(R))) / (f(L) - f(R)))
    print(R)
    print(f(R))
