def modulo_power(base, power, MOD):
    result = 1 % MOD

    for i in range(power):
        result = (result * base) % MOD

    return result


print(modulo_power(2, 10, 1000))
print(modulo_power(7, 0, 13))
print(modulo_power(9, 1, 7))
print(modulo_power(3, 4, 1))
print(modulo_power(0, 5, 11))
