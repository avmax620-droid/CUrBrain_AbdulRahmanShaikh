def digit_frequency_difference(n, a, b):
    count_a = 0
    count_b = 0

    if n == 0:
        if a == 0:
            count_a = 1

        if b == 0:
            count_b = 1

        return abs(count_a - count_b)

    while n > 0:
        digit = n % 10

        if digit == a:
            count_a += 1

        if digit == b:
            count_b += 1

        n = n // 10

    return abs(count_a - count_b)


print(digit_frequency_difference(112231, 1, 2))
print(digit_frequency_difference(55555, 5, 2))
print(digit_frequency_difference(123456, 3, 6))
print(digit_frequency_difference(0, 0, 5))
print(digit_frequency_difference(1002001, 0, 1))
