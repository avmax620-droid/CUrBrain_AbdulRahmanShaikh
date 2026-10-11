def is_prime(x):
    if x < 2:
        return False

    i = 2

    while i * i <= x:
        if x % i == 0:
            return False

        i += 1

    return True


def next_prime(n):
    candidate = max(2, n + 1)

    while True:
        if is_prime(candidate):
            return candidate

        candidate += 1


# Test cases
print(next_prime(14))  # 17
print(next_prime(0))   # 2
print(next_prime(1))   # 2
print(next_prime(2))   # 3
print(next_prime(17))  # 19
