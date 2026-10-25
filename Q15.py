def minimum_absolute_value(arr):
    minimum = arr[0]

    for value in arr:
        if abs(value) < abs(minimum):
            minimum = value

    return minimum


print(minimum_absolute_value([10, -5, -2, 4, 2]))
print(minimum_absolute_value([-3, 3]))
print(minimum_absolute_value([0, -1, 1]))
print(minimum_absolute_value([7, -7, 4]))
print(minimum_absolute_value([5, -2, 2, -1]))
