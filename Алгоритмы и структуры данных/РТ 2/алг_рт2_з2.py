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


def razlozh(a):
    itog = []
    b = 18
    if a in eretosfen(a):
        return f"{a} ** 1"
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0 and (i in eretosfen(i)):
                c = 0
                b = a
                while b % i == 0:
                    c += 1
                    b = b // i
                itog.append(f"{i} ** {c}")

                i = a // i
                if a % i == 0 and (i in eretosfen(i)):
                    c = 0
                    b = a
                    while b % i == 0:
                        c += 1
                        b = b // i
                    itog.append(f"{i} ** {c}")

    return " * ".join(itog)


print(razlozh(17))
print(razlozh(18))
