from time import time

def mult_on_1_figure(n_max, n_min): # давать числа фомата [0,9,9], 9
    n_inbrain = [0] * (len(n_max) + 1)
    n_itog = [0] * (len(n_max) + 1)

    for i in range(1, len(n_max) + 1):
        tr = (n_max[-i] * n_min + n_inbrain[-i])
        n_itog[-i] = tr % 10
        n_inbrain[-i-1] = tr // 10

    return n_itog

def sum_2(n_max, n_min):
    n_inbrain = [0] * (len(n_max) + 1)
    n_itog = [0] * (len(n_max) + 1)
    n_min = ([0] * (len(n_max) - len(n_min))) + n_min
    # print(n_itog, n_min)
    for i in range(1, len(n_max)+1):
        tr = (n_max[-i] + n_min[-i] + n_inbrain[-i])
        n_itog[-i] = tr % 10
        n_inbrain[-i-1] = tr // 10
    n_itog[0] = n_inbrain[0]
    if n_itog[0] == 0:
        n_itog.pop(0)
    return n_itog


def mult_2_num(n_max, n_min):
    n_inbrain = [0] * (len(n_max) + 1) * 2
    n_itog = [0] * (len(n_max) + 1) * 2

    for i in range(1, len(n_max) + 1):
        n_itog = sum_2(n_itog, mult_on_1_figure(n_max, n_min[-i]) + ([0] * (i - 1)))
    while n_itog[0] == 0:
        n_itog.pop(0)
    return n_itog

def format_nums(n1: str, n2: str):
    if len(n1) == len(n2):
        n_max = max(n1, n2)
        n_min = min(n1, n2)
    else:
        n_max = n1 if len(n1) > len(n2) else n2
        n_min = n1 if len(n1) < len(n2) else n2
        n_min = "0" * (len(n_max)-len(n_min)) + n_min
    n_max = [0] + list(map(int, list(n_max)))
    n_min = [0] + list(map(int, list(n_min)))
    return n_max, n_min

def mult(n1: str, n2: str):
    if len(n1) == n1.count("0") or len(n2) == n2.count("0"):
        return "0"
    if n1[0] == "-" and n2[0] == "-":
        n1 = n1[1:]
        n2 = n2[1:]    
        n_max = format_nums(n1, n2)[0]
        n_min = format_nums(n1, n2)[1]

        return  "".join(map(str, mult_2_num(n_max, n_min)))
    
    elif (n1[0] == "-") + (n2[0] == "-") == 1:
        n1 = n1[1:] if n1[0] == "-" else n1
        n2 = n2[1:] if n2[0] == "-" else n2
        n_max = format_nums(n1, n2)[0]
        n_min = format_nums(n1, n2)[1]
        
        return  "-" + "".join(map(str, mult_2_num(n_max, n_min)))
    
    else:
        n_max = format_nums(n1, n2)[0]
        n_min = format_nums(n1, n2)[1]
        
        return "".join(map(str, mult_2_num(n_max, n_min)))

# # a = time()
# print(mult("9"*4000, "9"*4000))
# # print(time()-a)
# print(mult("-999", "99"))
# print(mult("-999", "-99"))


