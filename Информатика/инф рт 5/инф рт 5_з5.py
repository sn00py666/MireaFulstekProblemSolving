def check_point(x, y):
    if x*x + y*y <= 1 and (x <= 0 or y >= x):
        return "yes" 
    return "no"

print(check_point(-0.1, -0.1))
print(check_point(0.1, -0.1))
