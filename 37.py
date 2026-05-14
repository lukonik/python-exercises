from collections import defaultdict

str1 = "swiss"

counter = defaultdict(int)

for i in str1:
    counter[i] = counter[i] + 1

for key, value in counter.items():
    if value == 1:
        print(key)
        break
