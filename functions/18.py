def apply_operation(fun, x, y):
    return fun(x, y)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print(f"Operations is: {apply_operation(add, 5, 3)}")
print(f"Multiply: {apply_operation(multiply, 2, 3)}")
