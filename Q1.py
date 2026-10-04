def count_digits(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count % 2 == 0


print(count_digits(1234))
print(count_digits(12345))
print(count_digits(0))
print(count_digits(-100000))
print(count_digits(-7))
