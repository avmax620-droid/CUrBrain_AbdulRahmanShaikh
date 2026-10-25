def threshold_filter(sales, threshold):
    result = []

    for value in sales:
        if value >= threshold:
            result.append(value)

    return result


print(threshold_filter([150, 80, 200, 90, 300], 100))
print(threshold_filter([100, 50, 100], 100))
print(threshold_filter([], 50))
print(threshold_filter([10, 20, 30], 40))
print(threshold_filter([75, 75, 75], 75))
