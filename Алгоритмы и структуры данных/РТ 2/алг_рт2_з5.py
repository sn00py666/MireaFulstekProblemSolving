def neiman(n):
    return str(int(n)**2)[2:7]
    

n = input()
for i in range(10):
    n = neiman(n)
    print(n)