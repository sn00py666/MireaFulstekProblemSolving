def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]

    lower_arr = [i for i in arr if i < pivot]
    higher_arr = [i for i in arr if i > pivot]

    return quick_sort(lower_arr) + [pivot] + quick_sort(higher_arr)

if __name__ == "__main__":
    print(quick_sort([6, 5, 4, 3, 2, 1]))
