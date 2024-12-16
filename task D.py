def task_D(arr, n):
    # Массив для максимальной подпоследовательности слева
    max_subseq_left = [0] * n
    # Массив для минимальной подпоследовательности слева
    min_subseq_left = [0] * n
    # Массив для префиксных сумм справа (не используется в расчетах, но может быть полезен)
    max_subseq_right = [0] * n
    # Массив для минимальной подпоследовательности справа
    min_subseq_right = [0] * n

    # Инициализация для первой позиции
    max_subseq_left[0] = arr[0]
    min_subseq_left[0] = arr[0]
    
    # Вычисление максимальной и минимальной подпоследовательности слева
    for i in range(1, n):
        max_subseq_left[i] = max(arr[i], max_subseq_left[i - 1] + arr[i])
        min_subseq_left[i] = min(arr[i], min_subseq_left[i - 1] + arr[i])
    
    # Вычисление минимальной подпоследовательности справа
    min_subseq_right[n - 1] = arr[n - 1]
    max_subseq_right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        max_subseq_right[i] = max(arr[i], max_subseq_right[i + 1] + arr[i])
        min_subseq_right[i] = min(arr[i], min_subseq_right[i + 1] + arr[i])

    res = 0
    for i in range(1,n):
        res = max(max_subseq_left[i - 1] - min_subseq_right[i], max_subseq_right[i] - min_subseq_left[i - 1], res)

    return res

# Ввод
n = int(input())
arr = [int(input()) for _ in range(n)]

# Вывод результата
print(task_D(arr, n))

# print("Максимальная подпоследовательность слева:", max_left)
# print("Минимальная подпоследовательность слева:", min_left)
# print("Максимальная подпоследовательность справа:", max_right)
# print("Минимальная подпоследовательность справа:", min_right)
