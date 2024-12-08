def shell_sort(arr):
    N = len(arr)
    d = N // 2

    while d > 0:
        for i in range(d, N):
            temp = arr[i]
            j = i
            while j >= d and arr[j - d] > temp:
                arr[j] = arr[j - d]
                j -= d
            arr[j] = temp
        d //= 2

    return arr

if __name__ == "__main__":
    print(shell_sort([6, 5, 4, 3, 2, 1]))
