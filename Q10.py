def count_primes(n):
    if n <= 2:
        return 0

    is_prime = [True] * n

    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p * p < n:
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False

        p += 1

    return sum(is_prime)


# Test cases
print(count_primes(10))  # 4
print(count_primes(2))   # 0
print(count_primes(0))   # 0
print(count_primes(3))   # 1
print(count_primes(30))  # 10
