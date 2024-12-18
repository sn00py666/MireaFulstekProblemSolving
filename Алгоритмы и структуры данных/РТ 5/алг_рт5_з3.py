def insertion_sort(arr):
    N = len(arr)
    
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

if __name__ == "__main__":
    print(insertion_sort([4,3,2,1]))