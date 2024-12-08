a = [[2, 30, 2, 3], [10, 2, 2, 2], [-3, 20, 2, 2], [-3, 20, 2, 2]]
b = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]


for i in range(len(a)):
    for j in range(len(a[i])):
        if i != 0 and j != 0:
            b[i][j] = max(a[i][j] + b[i-1][j], a[i][j] + b[i][j-1])      
        elif i == 0 and j == 0:
            b[i][j] = a[i][j]
        elif i == 0:
            b[i][j] = a[i][j] + b[i][j-1]
        elif j == 0:
            b[i][j] = a[i][j] + b[i-1][j]

for i in b:
    print(i)

i = len(b)-1
j = len(b[i])-1
print()
itog = [[i, j]]
while i != 0 or j != 0:
    if i != 0 and j != 0:
        if b[i-1][j] > b[i][j-1]:
            i -= 1
        else:
            j -= 1
    elif i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    itog.append([i,j])


for i in range(1, len(itog) + 1):
    print(itog[-i])