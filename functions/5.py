def func(a: int, b: int):
    def inner_func():
        return a + b

    return inner_func() + 5


print(func(5, 10))
