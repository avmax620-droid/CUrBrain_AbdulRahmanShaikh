def subtract_product_sum(n):
    digit_sum = 0
    digit_product = 1

    while n > 0:
        digit = n % 10

        digit_sum = digit_sum + digit
        digit_product = digit_product * digit

        n = n // 10

    return digit_product - digit_sum


print(subtract_product_sum(234))
print(subtract_product_sum(123))
print(subtract_product_sum(5))
print(subtract_product_sum(100))
print(subtract_product_sum(999))
