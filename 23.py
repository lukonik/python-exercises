d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

common = set(d1) & set(d2)

print(common)