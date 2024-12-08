def two_ch(n1, n2, n3):
    if (n1 % 2 == 0) + (n2 % 2 == 0) + (n3 % 2 == 0) >= 2:
        return "yes"
    return "no"

print(two_ch(4, 6, 123))
print(two_ch(13, 165, 4))
print(two_ch(2, 4, 8))