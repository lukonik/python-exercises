from typing import Sequence


def sort_odd_even(data: Sequence):
    print(f"Odd numbers {[value for value in data if value % 2 != 0]}")
    print(f"Even numbers {[value for value in data if value % 2 == 0]}")


sort_odd_even([12, 7, 34, 21, 5, 10, 8, 3, 19, 2])