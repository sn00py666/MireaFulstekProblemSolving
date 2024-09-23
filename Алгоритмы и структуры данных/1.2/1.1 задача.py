def binary_search(list, key):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        midVal = list[mid]
        if midVal == key:
            return mid
        if midVal > key:
            high = mid - 1
        else:
            low = mid + 1
    list.insert(low, key)
    
    return low, list

a = [1,2,3,4,5,6,8]
print(binary_search(a, 7))

a = [1,2,3,4,5,6,7,8]
print(binary_search(a, 7))
