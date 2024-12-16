import random


def task3(arr):
    counter_0 = 0
    res_2 = False
    res_3 = False
    for i in arr:
        if i == 0:
            counter_0 += 1
            if counter_0 == 2:
                res_2 = True
            if counter_0 == 3:
                res_3 = True            
        else:
            counter_0 = 0

    print("а) " + str(res_2))
    print("б) " + str(res_3))


# n = int(input())
# arr = [int(input()) for _ in range(n)]
# task3(arr)

task3([random.randint(-1,3) for _ in range(100)])

# task3([1,212000,0,2,4,0,2,0])
# print()
# task3([1,2,0,0,2,0])
# print()
# task3([1,20,0,0,0,2,4,0,2,0])
