from math import sin


def check_point(x, y):
    if y >= 0 and sin(x) <= 0.5:
        return "yes" 
    return "no"

print(check_point(1,1))
print(check_point(0.5,0.5))
print(check_point(0.4,0.4))
print(check_point(2,2))