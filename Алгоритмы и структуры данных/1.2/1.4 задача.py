def magic(list):
    itog = [0]*len(list)
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                itog[i] += 1
    return itog

print(magic([5,2,6,1]))
print(magic([5,5,5,5]))
print(magic([1,2,3,4]))