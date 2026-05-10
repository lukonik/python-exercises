def divide_numbers(a: int, b: int):
    try:
        return a / b
    except TypeError:
        print(f"Invalid value types: {a}, {b}")
    except ZeroDivisionError:
        print(f"Zero division not possible")
    finally:
        print("Operation complete")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "apple")
