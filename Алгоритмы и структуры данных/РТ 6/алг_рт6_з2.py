import random


def task2(arr):
    print(sum(list(filter(lambda x: x % 5 == 0 and x % 7 != 0, arr))))


# n = int(input())
# arr = [int(input()) for _ in range(n)]
# task1(arr)

task2([random.randint(1,1000) for _ in range(100)])