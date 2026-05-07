from typing import Sequence


def maxima(data: Sequence[float]):
    min = None
    max = None

    for value in data:
        if min is None:
            min = value
        elif min > value:
            min = value

        if max is None:
            max = value
        elif max < value:
            max = value

    print(f"MAX: {max}, MIN: {min}")


print(maxima([45, 2, 89, 12, 7]))
