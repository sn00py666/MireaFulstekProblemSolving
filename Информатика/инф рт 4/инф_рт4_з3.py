a = int(input())
k = int(input())

print(a)
a = a | 1 << (k - 1)
print(a)
