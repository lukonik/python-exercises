data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

result = []

for index in range(0, len(data), n):
    result.append(data[index : index + 3])


print(result)
