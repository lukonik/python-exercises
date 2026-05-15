data = {
    "fruits": ["apple", "banana", "cherry"],
    "vegs": ["carrot"],
    "grains": ["rice", "wheat"],
}


max_item = max(data, key=lambda key: len(data[key]))

print(max_item)