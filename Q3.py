def palindrome_or_sum(n):
    original = n
    sign = 1

    if n < 0:
        sign = -1
        n = abs(n)

    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    reverse = reverse * sign

    if original >= 0 and original == reverse:
        return original
    else:
        return original + reverse


print(palindrome_or_sum(121))
print(palindrome_or_sum(123))
print(palindrome_or_sum(0))
print(palindrome_or_sum(-45))
print(palindrome_or_sum(120))
