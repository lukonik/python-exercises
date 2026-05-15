data = [1, 2, 3, 4, 5]
k = 2
length = len(data)

k = k % length


result = data[k:] + data[:k]

print(result)
