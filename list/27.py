from collections import Counter

data = [1, 3, 3, 2, 1, 1, 4, 3, 3]

counter = Counter()

for item in data:
    counter[item] += 1


max_item = max(counter, key=lambda key: counter[key])

print(max_item)
