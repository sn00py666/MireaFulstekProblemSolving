def selection_sort(arr):
    N = len(arr)
    
    for i in range(0, N):
        m = float("inf")
        ind_m = -1
        for j in range(i, N):
            if arr[j] < m:
                m = arr[j]
                ind_m = j
        arr[i], arr[ind_m] = arr[ind_m], arr[i]

    return arr

if __name__ == "__main__":
    print(selection_sort([4,3,2,1]))