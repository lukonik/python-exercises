from collections import Counter


def word_frequency(text: str):
    words = [word.lower() for word in text.replace(".", "").split(" ")]
    counter_dict = Counter(words)
    return counter_dict

text = "Python is great. Python is fast, and learning Python is fun!"
print(word_frequency(text))
