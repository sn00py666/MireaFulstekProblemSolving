from алг_рт3_з5 import karatsuba
from алг_рт3_з1 import sum_2, subs_2


def div_2(n):
    result = []
    carry = 0
    for digit in n:
        current = carry * 10 + digit
        result.append(current // 2)
        carry = current % 2

    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    return result


def le(n1, n2):
    if len(n1) != len(n2):
        return len(n1) < len(n2)

    for d1, d2 in zip(n1, n2):
        if d1 != d2:
            return d1 < d2
    return True


def lt(n1, n2):
    if len(n1) != len(n2):
        return len(n1) < len(n2)

    for d1, d2 in zip(n1, n2):
        if d1 != d2:
            return d1 < d2
    return False


def divide_half(a, b):
    if b == [0]:
        raise ValueError("Деление на ноль!")
    if lt(a, b):
        return [0], a

    low, high = [0], a
    while le(low, high):
        mid = div_2(sum_2(low, high))
        product = karatsuba(mid, b)

        if product == a:
            return mid, [0]
        elif lt(product, a):
            low = sum_2(mid, [1])
        else:
            high = subs_2(mid, [1])

    return high, subs_2(a, karatsuba(high, b))


n1 = [int(elem) for elem in input("Первое оч большое двоичное число: ")]
n2 = [int(elem) for elem in input("Второе оч большое двоичное число: ")]

quotient, remainder = divide_half(n1, n2)
quotient, remainder = "".join(map(str, quotient)), "".join(map(str, remainder))
print(f"Частное: {quotient}, Остаток: {remainder}")
