import random


def task1(arr):
    print("a) " + str(len(list(filter(lambda x: x % 2 == 1, arr)))))
    print("б) " + str(len(list(filter(lambda x: x ** 0.5 == int(x ** 0.5) and x ** 0.5 % 2 == 0, arr)))))
    print("в) " + str(len(list(filter(lambda x: x % 3 == 0 and x % 5 != 0, arr)))))
    print("г) " + str(len(list(filter(lambda x: 2**x[0] < x[1] < x[0], enumerate(arr))))))
    print("д) " + str(len(list(filter(lambda x: x[1] < (arr[x[0]-1] + arr[0] + 1) / 2 and x[0] != 0 and x[0] != len(arr)-1, enumerate(arr))))))
    print("г) " + str(len(list(filter(lambda x: x[0] % 2 == 0 and x[1] % 2 == 1, enumerate(arr))))))

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# task1(arr)

task1([random.randint(1,1000) for _ in range(100)])