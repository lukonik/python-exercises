from functools import reduce

data = [2, 3, 5, 7]

print(reduce(lambda curr, prev: curr * prev, data, 1))
