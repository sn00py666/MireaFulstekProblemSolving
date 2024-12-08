def sundaram(n):
    new_n = (n-1)//2
    arr = [i for i in range(1, (n-1)//2+1)]
    for i in range(1, new_n+1):
        for j in range(1, new_n+1):
            if i + j + 2 * i * j > len(arr):
                break
            elif i + j + 2 * i * j in arr:
                arr[(i + j + 2 * i * j)-1] = 0
    arr = list(filter(lambda x: x != 0, arr))
    arr = list(map(lambda x: x*2 + 1, arr))
    return arr


print(sundaram(int(input())))
# print(sundaram(100))





    