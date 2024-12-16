def count_triangles(P, Q):
    count = 0
    for c in range(P, Q + 1):
        for a in range(P, c + 1):
            for b in range(a, c + 1):
                if a + b > c:
                    count += 1
    return count


P = int(input())
Q = int(input())

print(count_triangles(P, Q))
