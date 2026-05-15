d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 99, "c": 3}


same = {key: value for (key, value) in d1.items() if d2.get(key) == value}

print(same)