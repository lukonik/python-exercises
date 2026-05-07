from typing import List


def string_filter(text: List[str]):
    return [word.upper() for word in text if len(word) >= 4]


words = ["apple", "bat", "cherry", "dog", "elderberry"]

print(string_filter(words))
