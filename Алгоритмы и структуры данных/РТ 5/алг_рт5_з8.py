from алг_рт5_з3 import insertion_sort
import time
import random

def binary_search(arr, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low  # Позиция, куда нужно вставить key


def insertion_sort_wint_binary(arr):
    N = len(arr)
    
    for i in range(1, N):      
        pos = binary_search(arr, arr[i], 0, i)
        # Вставим элемент в найденную позицию
        arr.insert(pos, arr.pop(i))

    return arr

# if __name__ == "__main__":
#     print(insertion_sort_wint_binary([4,3,2,1]))

arr = random.sample(random(1, 10 ** 5), 10 ** 4)

time_small_insertion_start = time.time()

time_big_bubble_start = time.time()
insertion_sort(arr.copy())
time_big_insertion = time.time() - time_small_insertion_start

time_big_bubble_start = time.time()
insertion_sort_wint_binary(arr.copy())
time_big_insertion = time.time() - time_small_insertion_start
