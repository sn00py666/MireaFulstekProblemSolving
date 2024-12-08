def sum_2(n_max, n_min):
    n_itog = [0] * (len(n_max) )
    n_perenos = [0] * (len(n_max) )

    # while 1 in n_perenos:
    for i in range(1, len(n_max)):
        tr = (n_max[-i] + n_min[-i])
        n_itog[-i] = tr % 2
        n_perenos[-i-1] = 1 if tr == 2 else 0
    n_max = n_itog
    n_min = n_perenos
    print(n_max)
    print(n_min)
    print()
    while 1 in n_min:
        n_itog = [0] * (len(n_max) )
        n_perenos = [0] * (len(n_max) )

        for i in range(1, len(n_max)):
            tr = (n_max[-i] + n_min[-i])
            n_itog[-i] = 1 if tr == 1 else 0
            n_perenos[-i-1] = 1 if tr == 2 else 0
        n_max = n_itog
        n_min = n_perenos
        print(n_itog)
        print(n_perenos)
        print()
    return n_max, n_min


def sum_big_2(n1, n2):
    if len(n1) == len(n2):
        n_max = max(n1, n2)
        n_min = min(n1, n2)
    else:
        n_max = n1 if len(n1) > len(n2) else n2
        n_min = n1 if len(n1) < len(n2) else n2
        n_min = "0" * (len(n_max)-len(n_min)) + n_min

    n_max = [0] * 2 + list(map(int, list(n_max)))
    n_min = [0] * 2+ list(map(int, list(n_min)))
    print(n_max)
    print(n_min)
    print()
    itog = list(sum_2(n_max, n_min))
    while itog[0][0] == 0:
        itog[0].pop(0)
        itog[1].pop(0)
    return itog

a = "1111111"
b = "1"
print("ответ без лишних ноливков: " + "".join(map(str, list(sum_big_2(a, b))[0])))
print()
a = "0100011100"
b = "0101110111"
print("ответ без лишних ноливков: " + "".join(map(str, list(sum_big_2(a, b))[0])))
