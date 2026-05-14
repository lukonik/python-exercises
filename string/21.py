from collections import Counter


def freq(text: str):
    cache = Counter()

    for letter in text:
        cache[letter] += 1
    return cache


str1 = "apple"

print(freq(str1))
