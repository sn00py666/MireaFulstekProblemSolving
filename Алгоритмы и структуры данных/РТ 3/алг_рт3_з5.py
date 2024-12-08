from time import time
import алг_рт3_з4


def sum_2(n1, n2):
    if len(n1) == len(n2):
        n_max = max(n1,n2)
        n_min = min(n1,n2)
    else:
        n_max = n1 if max(len(n1),len(n2)) else n2
        n_min = [0] * len(n_max) + n2 if max(len(n1),len(n2)) else [0] * len(n_max) + n1


    n_inbrain = [0] * (len(n_max) + 1)
    n_itog = [0] * (len(n_max) + 1)

    for i in range(1, len(n_max)+1):
        tr = (n_max[-i] + n_min[-i] + n_inbrain[-i])
        n_itog[-i] = tr % 10
        n_inbrain[-i-1] = tr // 10
    n_itog[0] = n_inbrain[0]
    if n_itog[0] == 0:
        n_itog.pop(0)
    return n_itog

def subs_2(n_max, n_min):
    n_inbrain = [0] * (len(n_max))
    n_itog = [0] * (len(n_max))
    n_min = [0] * (len(n_max) - len(n_min)) + n_min

    for i in range(1, len(n_max)+1):
        if n_max[-i] + n_inbrain[-i] < n_min[-i]:
            n_inbrain[-i] += 10
            n_inbrain[-i - 1] += -1
        n_itog[-i] = n_max[-i] + n_inbrain[-i] - n_min[-i]
    if len(set(n_itog)) == 1 and  set(n_itog).pop() == 0:
        return [0]
    else:
        while n_itog[0] == 0:
            n_itog.pop(0)
    return n_itog

# def subs_2(n_max, n_min):
#     n_itog = int("".join(list(map(str, n_max)))) - int("".join(list(map(str, n_min))))
#     n_itog = list(map(int, list(str(n_itog))))
#     return n_itog


def formatirovanie(n1,n2):
    n1 = n1 if len(n1) % 2 == 0 else [0] + n1
    n2 = n2 if len(n2) % 2 == 0 else [0] + n2
    max_len = max(len(n1), len(n2))
    n1 = [0] * (max_len - len(n1)) + n1
    n2 = [0] * (max_len - len(n2)) + n2

    return n1, n2


def karatsuba_vnutr(n1, n2):
    formats = formatirovanie(n1, n2)
    n1 = formats[0]
    n2 = formats[1]

    if len(n1) <= 2:
        res = list(map(int, list(str(int("".join(map(str,n1))) * int("".join(map(str,n2)))))))
        if len(res) % 2 == 0:
            return res
        else: return [0] + res
    
    a = n1[:len(n1) // 2]
    b = n1[len(n1) // 2:]
    c = n2[:len(n2) // 2]
    d = n2[len(n2) // 2:]

    ac = karatsuba_vnutr(a,c)
    bd = karatsuba_vnutr(b,d)
    ac_x_2 = ac + [0] * len(n1)

    apb_cpd = karatsuba_vnutr(sum_2(a, b),sum_2(c,d))
    apb_cpd_mac_mbd_x = subs_2(subs_2(apb_cpd, ac), bd) + [0] * (len(n1)//2)
    
    return sum_2(sum_2(ac_x_2, apb_cpd_mac_mbd_x), bd)


# def karatsuba2(n1, n2):
#     res = "".join(list(map(str, karatsuba_vnutr(list(map(int,list(n1))), list(map(int, list(n2)))))))
#     while res[0] == "0":
#         res = res[1:]
#     return res

def karatsuba(n1, n2):
    res = karatsuba_vnutr(n1, n2)
    # res = karatsuba_vnutr(list(map(int,list(n1))), list(map(int, list(n2))))
    while res[0] == 0:
        res = res[1:]
    return res


# print(sum_2([0,0,0,3], [0,6,5,6]))
# print(karatsuba("37656", "6567863"))


# t1 = time()
# print(karatsuba([1, 1], [1, 1]))
# t_karats = (time() - t1)

# t2 = time()
# print(алг_рт3_з4.mult("9"*7000, "9"*6000))
# t_base = time() - t2
# print(t_karats, t_base)
# print(karatsuba_vnutr([7,6,5,6], [7,8,6,3]))
