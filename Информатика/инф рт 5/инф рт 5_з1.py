def tr_pol(n):
    if n == abs(n) and n % 5 == 0 and len(str(abs(n))) == 3:
        return "yes"
    return "no"

print(tr_pol(125))
print(tr_pol(-125))
print(tr_pol(1235))
