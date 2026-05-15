from collections import Counter

data = [10, 20, 30, 10, 40, 10, 50]

counter = Counter()


for item in data:
    counter[item] += 1

print(max(counter, key=lambda key: counter[key]))
