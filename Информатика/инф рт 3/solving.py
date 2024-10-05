import math
x = 1
hx = 0.5
y = 1
hy = 1
def f(x, y):
    if x + y <= 2: return math.sin(x*math.e**(0.1*y))**(1/3)
    else: return abs(math.log(x+y, 2))

for xn in range(4):
    x = x + hx * xn
    for yn in range(4):
        y = y + hy * yn
        print(f(x,y))