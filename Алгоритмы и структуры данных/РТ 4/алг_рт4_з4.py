def sum_of_digits(n):
    return n % 10 + sum_of_digits(n // 10) if n >= 10 else n


print(sum_of_digits(10001))