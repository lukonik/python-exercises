def max(lst: list[int]):
    max = None

    for i in lst:
        if max is None:
            max = i
        elif i > max:
            max = i
    return max


x = [4, 6, 8, 24, 12, 2]

print(max(x))