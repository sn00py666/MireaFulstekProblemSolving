def shaker_sort(arr):
    N = len(arr)
    
    low, up = 0, N - 1
    last = -1
    
    while low < up:
        last = -1
        for i in range(low, up):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last = i
        
        up = last
        if last == -1:
            break
        
        last = N
        for i in range(up - 1, low - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last = i
        
        low = last + 1
    
    return arr

if __name__ == "__main__":
    print(shaker_sort([4,3,2,1]))