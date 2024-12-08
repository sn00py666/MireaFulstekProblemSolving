def sum_two(mas, goal):
    hash_table={}
    for i, num in enumerate(mas):
        temp = goal - num
        if temp in hash_table:
            return (hash_table[temp], i)
        hash_table[num] = i
    return None
mas = [-1, 3, 2, 4, 7, 1]
goal = 5
res = sum_two(mas, goal)
print(res)
