def base_n(A, n):
    if A == 0:
        return "0"

    digits = []
    while A > 0:
        remainder = A % n
        digits.append(str(remainder))
        A = A // n
    digits.reverse()
    return ''.join(digits)


A = int(input("Введите число A: "))
n = int(input("Введите основание системы счисления n (2 ≤ n ≤ 9): "))

if A >= 2**31:
    print("Ошибка: число A должно быть меньше 2^31.")
elif not (2 <= n <= 9):
    print("Ошибка: основание системы счисления должно быть в диапазоне от 2 до 9.")
else:
    result = base_n(A, n)
    print(f"Число {A} в системе счисления с основанием {n} равно: {result}")
