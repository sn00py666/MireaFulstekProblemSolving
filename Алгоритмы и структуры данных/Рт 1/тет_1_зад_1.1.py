# точность 0.0001
import math

R = 1
L = 0
B = 0

while R-L > 0.0001:
    B = L + ((R-L) / 2)
    if (math.acos(B) - math.sqrt(1 - 0.3 * B ** 3)) * (math.acos(R) - math.sqrt(1 - 0.3 * R ** 3)) < 0:
        L = B
    else:
        R = B
print()
print(B)
print((math.acos(B) - math.sqrt(1 - 0.3 * B ** 3)))
