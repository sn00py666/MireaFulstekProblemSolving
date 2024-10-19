from sys import stdin


def marsen(p):
    return  (2 ** p) - 1


def luka_lemar(p):
    k = p - 1
    s = 4
    for _ in range(k-1):
        s = s**2 - 2
    if s % marsen(p) == 0:
        return "Простое", marsen(p)
    else: return "Не простое", marsen(p)


for num in stdin:
    print(luka_lemar(int(num)))
