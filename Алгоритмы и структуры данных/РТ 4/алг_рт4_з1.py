def NOD_evklid(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return a + b

    if a > b:
        return NOD_evklid(a-b, b)
    elif b > a:
        return NOD_evklid(a, (b-a))
    else:
        return a
    
print(NOD_evklid(-50, 0))