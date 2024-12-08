def hash_table_init(arr):
    hash_table = [None] * len(arr)
    table_size = len(arr)
    for num in arr:
        hash_value = num % 7
        if hash_table[hash_value] == None:
            hash_table[hash_value] = num
        else:
            i = (hash_value + 1) % table_size
            while hash_table[i] != None:
                i = (i + 1) % table_size
            hash_table[i] = num

    return hash_table


a = [86, 90, 27, 29, 38, 39, 40]
print(hash_table_init(a))