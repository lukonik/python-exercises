from itertools import combinations


def power_set(lst: list):
    response = []
    for i in range(len(lst) + 1):
        response.extend(combinations(lst, i))
    return response


data = [1, 2, 3]

print(power_set(data))
