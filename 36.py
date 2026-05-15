original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

inverted = {}

for key, value in original.items():
    inverted.setdefault(value, []).append(key)

print(inverted)
