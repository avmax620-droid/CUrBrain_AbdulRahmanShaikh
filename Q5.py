def replace_even_digits(n):
    digits = []

    while n > 0:
        digit = n % 10

        if digit % 2 == 0:
            digits.append(0)
        else:
            digits.append(digit)

        n = n // 10

    digits.reverse()

    return digits


print(replace_even_digits(258))
print(replace_even_digits(12345))
print(replace_even_digits(2468))
print(replace_even_digits(13579))
print(replace_even_digits(1002))
