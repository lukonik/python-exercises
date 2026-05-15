data = [0, 1, 0, 3, 12]


non_zero = [item for item in data if item != 0]

zero = [item for item in data if item == 0]

result = non_zero + zero

print(result)
