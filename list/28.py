data = ["a", "b", "c", "d", "e", "f", "g"]
n = 3

updated = [value for (index, value) in enumerate(data) if index % n == 0]

print(updated)
