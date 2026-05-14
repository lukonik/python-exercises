sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = len(sample_list) // 3

first = sample_list[:chunk_size]
second = sample_list[chunk_size : chunk_size * 2]
third = sample_list[chunk_size * 2 :]


print(first)
print(second)
print(third)