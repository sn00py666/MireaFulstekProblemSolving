def bubble_sort(arr):
    n = len(arr)

    # Сортировка пузырьком
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    print(bubble_sort([4,3,2,1]))
