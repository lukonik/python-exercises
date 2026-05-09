def binary_search(lst: list, low: int, high: int, target: int):
    mid = (low + high) // 2

    if low > high:
        return -1

    if not len(lst) < mid:
        return -1

    if lst[mid] == target:
        return mid

    if lst[mid] > target:
        return binary_search(lst, low, mid, target)

    else:
        return binary_search(lst, mid + 1, high, target)


lst = [10, 20, 30, 40, 50, 60]

print(binary_search(lst, 0, len(lst), 12312))
