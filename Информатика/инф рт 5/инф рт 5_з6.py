from math import sin


def check_point3(x, y):
    return "yes" if x > 0 and ((x*x + y*y <= 1) or (y <= 1 and y >= x-1)) else "no"


def check_point4(x, y):
    return "yes" if y >= 0 and sin(x) <= 0.5 else "no"


def check_point5(x, y):
    return "yes" if x*x + y*y <= 1 and (x <= 0 or y >= x) else "no"


print(check_point3(1,1))
print(check_point3(0.5,0.5))
print(check_point3(2,2))
print()
print(check_point4(1,1))
print(check_point4(0.5,0.5))
print(check_point4(0.4,0.4))
print(check_point4(2,2))
print()
print(check_point5(-0.1, -0.1))
print(check_point5(0.1, -0.1))
