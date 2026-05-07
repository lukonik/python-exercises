def square_dict(range_stop: int):
    return {value: value**2 for value in range(1, range_stop)}


print(square_dict(10))
