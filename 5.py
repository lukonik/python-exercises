from typing import List


def flatten(data: List):
    flattened = []

    def rec(items: List):
        for item in items:
            if isinstance(item, list):
                rec(item)
            else:
                flattened.append(item)

    rec(data)
    return flattened


nested = [1, [2, 3], [4, [5, 6]], 7]

print(flatten(nested))
