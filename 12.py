from typing import List


def same_first_and_last(data: List[int]):
    return data[0] == data[-1]

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(same_first_and_last(numbers_x))
print(same_first_and_last(numbers_y))