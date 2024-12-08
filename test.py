# Сортировка массивов с учетом частоты: Создайте массив NxM (N и M вводятся с 
# клавиатуры). Необходимо отсортировать его таким образом, чтобы элементы, которые 
# имеют более высокую частоту появления, располагались впереди, а элементы с 
# одинаковой частотой упорядочивались по возрастанию.
# Например, для массива [1, 2, 2, 3, 1, 4, 3, 3] ожидаемый результат будет [3, 3, 3, 1, 1, 2, 2, 4].

import numpy as np


def lenght(arr: list) -> int:
    c = 0
    for _ in arr: c += 1
    return c


def sort_for_freq(arr: np.ndarray) -> np.ndarray:
    frequency = {i: {} for i in range(lenght(arr))}
    for i in range(lenght(arr)):
        for j in range(lenght(arr[i])):
            if arr[i][j] in frequency[i]:
                frequency[i][arr[i][j]] += 1
            else:
                frequency[i][arr[i][j]] = 1

    output = []

    for i in frequency:
        temp_arr = []
        sub_d: dict = frequency[i]
        k = list(sub_d.keys())
        v = list(sub_d.values())

        for i in range(len(k)):
            for j in range(i + 1, len(k)):
                if k[i] > k[j]:
                    k[i], k[j] = k[j], k[i]
        
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                if v[i] > v[j]:
                    v[i], v[j] = v[j], v[i]

        for count in v[::-1]:
            for num in k:
                if num in sub_d:
                    if sub_d[num] == count:
                        for _ in range(count):
                            temp_arr.append(num)
                        sub_d.pop(num)

        output.append(temp_arr)

    return np.array(output)


N = int(input("Кол-во строк: "))
M = int(input("Кол-во столбцов: "))
a = int(input("Минимально значение генерируемого числа: "))
b = int(input("Максимальное значение генерируемого числа (не учитывается): "))

arr = np.random.randint(a, b, size=(N, M))
print(f"Исходный массив: {arr}")

sorted_arr = sort_for_freq(arr)
print(sorted_arr)
