from functools import reduce


def exp(base: int, exp: int):
    return reduce(lambda pr, _: pr * base, range(exp), 1)


print(exp(2, 4))
