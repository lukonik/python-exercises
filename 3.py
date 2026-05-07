from collections import Counter


def char_counter(text: str):
    return Counter(text.lower().replace(" ", ""))


print(char_counter("Python Programming"))
