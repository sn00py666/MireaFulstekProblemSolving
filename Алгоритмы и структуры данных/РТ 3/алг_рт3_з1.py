def normalization(n1, n2):
    if len(n1) < len(n2):
        n1 = [0] * (len(n2) - len(n1)) + n1
    else:
        n2 = [0] * (len(n1) - len(n2)) + n2
    return n1, n2

# def sum_2(n_max, n_min):
#     n_inbrain = [0] * (len(n_max) + 1)
#     n_itog = [0] * (len(n_max) + 1)

#     for i in range(1, len(n_max)+1):
#         tr = (n_max[-i] + n_min[-i] + n_inbrain[-i])
#         n_itog[-i] = tr % 10
#         n_inbrain[-i-1] = tr // 10
#     n_itog[0] = n_inbrain[0]
#     if n_itog[0] == 0:
#         n_itog.pop(0)
#     return "".join(map(str, n_itog))

def sum_2(n_max, n_min):
    n_max, n_min = normalization(n_max, n_min)
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


# def subs_2(n_max, n_min):
#     n_inbrain = [0] * (len(n_max))
#     n_itog = [0] * (len(n_max))

#     for i in range(1, len(n_max)+1):
#         if n_max[-i] + n_inbrain[-i] < n_min[-i]:
#             n_inbrain[-i] += 10
#             n_inbrain[-i - 1] += -1
#         n_itog[-i] = n_max[-i] + n_inbrain[-i] - n_min[-i]
#     while n_itog[0] == 0:
#         n_itog.pop(0)
#     return "".join(map(str, n_itog))


def subs_2(n_max, n_min):
    n_max, n_min = normalization(n_max, n_min)
    n_inbrain = [0] * (len(n_max))
    n_itog = [0] * (len(n_max))

    for i in range(1, len(n_max)+1):
        if n_max[-i] + n_inbrain[-i] < n_min[-i]:
            n_inbrain[-i] += 10
            n_inbrain[-i - 1] += -1
        n_itog[-i] = n_max[-i] + n_inbrain[-i] - n_min[-i]
    while n_itog[0] == 0:
        n_itog.pop(0)
    return n_itog


def sum_big_n(n1, n2):
    if n1[0] == "-" and n2[0] == "-":
        n1 = n1[1:]
        n2 = n2[1:]
        if len(n1) == len(n2):
            n_max = max(n1, n2)
            n_min = min(n1, n2)
        else:
            n_max = n1 if len(n1) > len(n2) else n2
            n_min = n1 if len(n1) < len(n2) else n2
            n_min = "0" * (len(n_max)-len(n_min)) + n_min

        n_max = list(map(int, list(n_max)))
        n_min = list(map(int, list(n_min)))
        return "-" + sum_2(n_max, n_min)
            
    elif n1[0] == "-" and n2[0] != "-":
        n1 = n1[1:]
        if len(n1) == len(n2):
            n_max = max(n1, n2)
            n_min = min(n1, n2)
        else:
            n_max = n1 if len(n1) > len(n2) else n2
            n_min = n1 if len(n1) < len(n2) else n2
            n_min = "0" * (len(n_max)-len(n_min)) + n_min

        znak = "" if n_max == n2 else "-"
        n_max = list(map(int, list(n_max)))
        n_min = list(map(int, list(n_min)))
        return znak + subs_2(n_max, n_min)
    
    elif n1[0] != "-" and n2[0] == "-":
        n2 = n2[1:]
        if len(n1) == len(n2):
            n_max = max(n1, n2)
            n_min = min(n1, n2)
        else:
            n_max = n1 if len(n1) > len(n2) else n2
            n_min = n1 if len(n1) < len(n2) else n2
            n_min = "0" * (len(n_max)-len(n_min)) + n_min

        znak = "" if n_max == n1 else "-"
        n_max = list(map(int, list(n_max)))
        n_min = list(map(int, list(n_min)))
        return znak + subs_2(n_max, n_min)

    else:
        if len(n1) == len(n2):
            n_max = max(n1, n2)
            n_min = min(n1, n2)
        else:
            n_max = n1 if len(n1) > len(n2) else n2
            n_min = n1 if len(n1) < len(n2) else n2
            n_min = "0" * (len(n_max)-len(n_min)) + n_min

        n_max = list(map(int, list(n_max)))
        n_min = list(map(int, list(n_min)))
        return sum_2(n_max, n_min)


def subs_big_n(n1, n2):
    if n1[0] == "-" and n2[0] == "-":
        n1 = n1[1:]
        n2 = n2[1:]
        if len(n1) == len(n2):
            n_max = max(n1, n2)
            n_min = min(n1, n2)
        else:
            n_max = n1 if len(n1) > len(n2) else n2
            n_min = n1 if len(n1) < len(n2) else n2
            n_min = "0" * (len(n_max)-len(n_min)) + n_min
        
        znak = "-" if n_max == n1 else ""
        n_max = list(map(int, list(n_max)))
        n_min = list(map(int, list(n_min)))
        return znak + subs_2(n_max, n_min) 
    
    elif n1[0] == "-" and n2[0] != "-":
        n1 = n1[1:]
        if len(n1) == len(n2):
            n_max = max(n1, n2)
            n_min = min(n1, n2)
        else:
            n_max = n1 if len(n1) > len(n2) else n2
            n_min = n1 if len(n1) < len(n2) else n2
            n_min = "0" * (len(n_max)-len(n_min)) + n_min
        
        n_max = list(map(int, list(n_max)))
        n_min = list(map(int, list(n_min)))
        return "-" + sum_2(n_max, n_min) 
    
    elif n1[0] != "-" and n2[0] == "-":
        n2 = n2[1:]
        if len(n1) == len(n2):
            n_max = max(n1, n2)
            n_min = min(n1, n2)
        else:
            n_max = n1 if len(n1) > len(n2) else n2
            n_min = n1 if len(n1) < len(n2) else n2
            n_min = "0" * (len(n_max)-len(n_min)) + n_min
        
        n_max = list(map(int, list(n_max)))
        n_min = list(map(int, list(n_min)))
        return sum_2(n_max, n_min) 
    
    else:
        if len(n1) == len(n2):
            n_max = max(n1, n2)
            n_min = min(n1, n2)
        else:
            n_max = n1 if len(n1) > len(n2) else n2
            n_min = n1 if len(n1) < len(n2) else n2
            n_min = "0" * (len(n_max)-len(n_min)) + n_min
        
        znak = "" if n_max == n1 else "-"
        n_max = list(map(int, list(n_max)))
        n_min = list(map(int, list(n_min)))
        return znak + subs_2(n_max, n_min) 

# print(subs_big_n("1" * 10000, "9" * 10000))
# print(sum_big_n("9" * 10000, "1" * 10000))

# print(sum_big_n("222", "99"))
# print(sum_big_n("222", "999"))
# print(sum_big_n("222", "9"))
# print(sum_big_n("-111", "15"))
# print(sum_big_n("111", "-15"))

# print(subs_big_n("-111", "-15"))
# print(subs_big_n("-111", "15"))
# print(subs_big_n("111", "-15"))
# print(subs_big_n("111", "15"))

# print(sum_big_n("11111"*10000, "9"*9999))

# print(subs_2([1,2], [0,3]))