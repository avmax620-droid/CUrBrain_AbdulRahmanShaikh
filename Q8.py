def kth_factor(n, k):
    factors = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)

            if i != n // i:
                factors.append(n // i)

    factors.sort()

    if k <= len(factors):
        return factors[k - 1]

    return -1


# Test cases
print(kth_factor(12, 3))  # 3
print(kth_factor(1, 1))   # 1
print(kth_factor(12, 6))  # 12
print(kth_factor(12, 7))  # -1
print(kth_factor(36, 5))  # 6
