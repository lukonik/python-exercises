from collections import Counter

text = "the cat sat on the mat the cat"

text_ins = text.lower()

counter = Counter(text.split(" "))


print(counter)