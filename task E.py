def task_E(n, t, arr_t, arr_n):
    res = 0
    if n == 1:
        res = t - arr_n[0] + 1
    return res


t = int(input())
n = int(input())
arr_t = [int(input()) for i in range(t)]
arr_n = [int(input()) for i in range(n)]
print(task_E(n, t, arr_t, arr_n))

