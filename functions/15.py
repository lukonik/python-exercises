from typing import Callable


def filter(numbers, predicate: Callable):
    return [value for value in numbers if predicate(value)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter(numbers, lambda x: x % 2 == 0))
