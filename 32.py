
words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}

print(dict(sorted(words.items(), key=lambda data: len(data[1]))))
