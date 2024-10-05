def eretosfen(n):
    arr = [i for i in range(2, n+1)]
    p = 2
    while arr != list(filter(lambda x: x % p != 0, arr)):
        i = 1
        while i < len(arr):
            if arr[i] != p and arr[i] % p == 0:
                arr.pop(i)
            i += 1
        if arr.index(p) < len(arr) - 1:
            p = arr[arr.index(p) + 1]
        else: break
    return arr

def ferma(n):
    n = n
    m = int(n**0.5)
    x = 0
    q = (m + x)**2 - n 
    
    while q ** 0.5 != int(q ** 0.5):
        x += 1
        q = (m + x)**2 - n 
    p1 = int(q**0.5 + (x + m))
    p2 = int((m + x) - q**0.5)
    itog = [p1,p2]
    
    if p1 not in eretosfen(p1):
        for i in list(ferma(p1)):
            itog.append(i)
        itog.remove(p1)    
    if p2 not in list(eretosfen(p2)):
        for i in ferma(p2):
            itog.append(i)
        itog.remove(p2)
        
    return itog

print(ferma(19691))
# print(ferma(1275))
# print(ferma(25))