from typing import List


def word_count(data: List[str]):
    return [(value, len(value)) for value in data]


print(word_count(["Apple", "Banana", "Cherry", "Date", "Elderberry"]))
