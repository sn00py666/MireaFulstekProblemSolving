import math

def min_rolls_needed(a, h, k, m, s):
    num_strips = math.ceil(a / m)
    len_one_strip = math.ceil(h / k) * k 
    strips_in_one_roll = s // len_one_strip
    itog = math.ceil(num_strips / strips_in_one_roll)
    return itog


# Пример 1
a = int(input())
h = int(input())
k = int(input())
m = int(input())
s = int(input())

print(min_rolls_needed(a, h, k, m, s))

