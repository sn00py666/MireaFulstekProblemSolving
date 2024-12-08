from алг_рт5_з1 import bubble_sort
from алг_рт5_з2 import shaker_sort
from алг_рт5_з3 import insertion_sort
from алг_рт5_з4 import selection_sort
from алг_рт5_з5 import shell_sort
from алг_рт5_з6 import quick_sort

import random
import time


arr_small = random.sample(range(1,1000), 500) 
arr_big = random.sample(range(1,10**7), 11**4)

# Пузырек
time_small_bubble_start = time.time()
bubble_sort(arr_small.copy())
time_small_bubble = time.time() - time_small_bubble_start

time_big_bubble_start = time.time()
bubble_sort(arr_big.copy())
time_big_bubble = time.time() - time_small_bubble_start

print("Пузырек маленький массив " + str(time_small_bubble))
print("Пузырек большой массив " + str(time_big_bubble))
print()


# Шейкер
time_small_shaker_start = time.time()
shaker_sort(arr_small.copy())
time_small_shaker = time.time() - time_small_shaker_start

time_big_shaker_start = time.time()
shaker_sort(arr_big.copy())
time_big_shaker = time.time() - time_small_shaker_start

print("Шейкер маленький массив " + str(time_small_shaker))
print("Шейкер большой массив " + str(time_big_shaker))
print()

# вставками
time_small_insertion_start = time.time()
insertion_sort(arr_small.copy())
time_small_insertion = time.time() - time_small_insertion_start

time_big_insertion_start = time.time()
insertion_sort(arr_big.copy())
time_big_insertion = time.time() - time_small_insertion_start

print("Вставкой маленький массив " + str(time_small_insertion))
print("Вставкой большой массив " + str(time_big_insertion))
print()

# Выбором
time_small_selection_start = time.time()
selection_sort(arr_small.copy())
time_small_selection = time.time() - time_small_selection_start

time_big_selection_start = time.time()
selection_sort(arr_big.copy())
time_big_selection = time.time() - time_small_selection_start

print("Выбором маленький массив " + str(time_small_selection))
print("Выбором большой массив " + str(time_big_selection))
print()

# Шелл
time_small_shell_start = time.time()
shell_sort(arr_small.copy())
time_small_shell = time.time() - time_small_shell_start

time_big_shell_start = time.time()
shell_sort(arr_big.copy())
time_big_shell = time.time() - time_small_shell_start

print("Шелл маленький массив " + str(time_small_shell))
print("Шелл большой массив " + str(time_big_shell))
print()

# Быстрая
time_small_quick_start = time.time()
quick_sort(arr_small.copy())
time_small_quick = time.time() - time_small_quick_start

time_big_quick_start = time.time()
quick_sort(arr_big.copy())
time_big_quick = time.time() - time_small_quick_start

print("Быстрая маленький массив " + str(time_small_quick))
print("Быстрая большой массив " + str(time_big_quick))
print()
