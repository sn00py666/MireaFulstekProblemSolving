def binary_search2(list):
    key = 0
    low = 0
    high = len(list) - 1
    while 0 in list:
        list.remove(0)
    while low <= high:
        mid = (low + high) // 2
        midVal = list[mid]
        if midVal == key:
            return max(mid, len(list) - 1 - mid)
        if midVal > key:
            high = mid - 1
        else:
            low = mid + 1
    list.insert(low, key)
    
    return max(low, len(list) - 1 - low)

a = [-5, -4, 1, 5, 6, 7, 8]
print(binary_search2(a))

a = [-6, -5, -4, -3, -2, -1, 2, 3, 4]
print(binary_search2(a))

a = [-5, 0, 0, 0, 1, 2, 3, 4]
print(binary_search2(a))
