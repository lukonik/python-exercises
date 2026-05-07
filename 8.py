from typing import List

vowels = set(["a", "e", "i", "o", "u"])


def only_start_with(words: List[str]):
    return [word for word in words if len(word) > 5 and word[0] in vowels]

print(only_start_with(["apple", "education", "ice", "ocean", "python", "umbrella"]))