def second_highest(scores):
    highest = None
    second_highest_score = None

    for score in scores:
        if highest is None or score > highest:
            second_highest_score = highest
            highest = score

        elif score != highest:
            if second_highest_score is None or score > second_highest_score:
                second_highest_score = score

    if second_highest_score is None:
        return -1

    return second_highest_score


print(second_highest([50, 40, 50, 30]))
print(second_highest([100, 100, 100]))
print(second_highest([]))
print(second_highest([10, 20, 30, 40]))
print(second_highest([5, 5, 4, 4, 3]))
