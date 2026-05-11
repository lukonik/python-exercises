from typing import List


def remove_duplicates(data: List[int]):
    seen = set()
    new_data: List[int] = []
    for item in data:
        if item not in seen:
            new_data.append(item)
        seen.add(item)
    return new_data

print(remove_duplicates([1, 2, 2, 3, 1, 4, 2]))
