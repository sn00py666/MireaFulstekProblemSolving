def gor(list):
    if len(list) < 3: return "Не горный"
    else:
        left = 0
        right = len(list) - 1

        while left <= right:
            mid = (left + right) // 2
            if mid == len(list)-1:
                break
            elif list[mid] > list[mid + 1]: right = mid - 1
            else: left = mid + 1
        if mid == 0: return "Не горный"
        elif mid == len(list)-1: return "Не горный"
        return left

print(gor([1,2,3,4,5,6]))
print(gor([6,5,4,3,2,1]))
print(gor([2,2,2,2,2,2]))
print(gor([1,2,3,4,2,1]))
