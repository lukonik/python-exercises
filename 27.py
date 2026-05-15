data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
keys = list(data.keys())
for key in keys:
    if data[key] is None:
        del data[key]

print(data)