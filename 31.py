main = {"a": 1, "b": 2, "c": 3, "d": 4}
subset = {"a": 1, "c": 3}

is_subset = subset.items() <= main.items()

print(is_subset)