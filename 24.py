def f(terms: int):
    num1, num2 = 0, 1

    for _ in range(terms):
        print(num1, end=" ")
        result = num1 + num2
        num1 = num2
        num2 = result


f(15)
