def check_point(x, y):
    if x > 0 and ((x*x + y*y <= 1) or (y <= 1 and y >= x-1)):
        return "yes"
    return "no"

print(check_point(1,1))
print(check_point(0.5,0.5))
print(check_point(2,2))