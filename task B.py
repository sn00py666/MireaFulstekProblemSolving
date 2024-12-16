# def task_B(arr):
#     arr = sorted(arr)
#     clicks = 0
#     for i in range(len(arr)):
#         clicks += min(arr[0] + 1, 1 + sum(arr) - arr[0] + 1)
#         # print(clicks, arr[0], arr)
#         arr.pop(0)
#     return clicks 

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# print(task_B(arr))


def task_B(arr):
    arr = sorted(arr)
    res = sum(arr[:-1]) + len(arr[:-1]) + 2
    return res


n = int(input())
arr = [int(input()) for _ in range(n)]
print(task_B(arr))