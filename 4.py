from collections import Counter

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

counter = Counter()

for item in sample_list:
    counter[item] += 1

print(counter)
