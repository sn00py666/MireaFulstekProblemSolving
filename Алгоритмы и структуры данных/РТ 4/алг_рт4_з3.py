import math

def f(x):
    return (math.acos(x) - math.sqrt(1 - 0.3 * x ** 3))

def pol_del(F, L, R):
    B = L + ((R-L) / 2)
    if abs(F(B)) < 0.00001:
        return B
    elif F(B) * F(R) < 0:
        return pol_del(f, B, R)
    else:
        return pol_del(f, L, B)


print(pol_del(f, 0, 1))