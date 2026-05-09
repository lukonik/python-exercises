def map_filter(lst: list[int]):
    return map(lambda x: x**2, filter(lambda y: y % 2 == 0, lst))


nums = [1, 2, 3, 4, 5, 6]


print(list(map_filter(nums)))
