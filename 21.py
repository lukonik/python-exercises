from typing import List


def find_duplicates(numbers: List[int]):
    duplicates = set()
    seen = set()
    for number in numbers:
        if number not in duplicates:
            duplicates.add(number)
        else:
            seen.add(number)
    return seen


numbers = [1, 2, 3, 2, 4, 5, 1, 6]
print(find_duplicates(numbers))
