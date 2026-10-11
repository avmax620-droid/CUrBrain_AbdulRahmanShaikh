import math

def array_gcd(arr):
    result = arr[0]

    for num in arr[1:]:
        result = math.gcd(result, num)

    return result


# Test cases
print(array_gcd([24, 36, 48]))       # 12
print(array_gcd([33, 44, 55, 66]))   # 11
print(array_gcd([17]))               # 17
print(array_gcd([12, 18, 24, 30]))   # 6
print(array_gcd([1, 7, 14, 28]))    # 1
