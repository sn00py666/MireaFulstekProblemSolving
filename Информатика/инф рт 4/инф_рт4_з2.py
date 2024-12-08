n = int(input())

if n == ((n >> len(str(bin(n)[2:]))-1) << len(str(bin(n)[2:])) - 1):
    print("YES")
else:
    print("NO")
