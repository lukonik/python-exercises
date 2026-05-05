def calculate_tax(income: int):
    if income < 10_000:
        return income

    if 10_000 <= income <= 20_000:
        return (income * 10) / 100

    return (income * 0.1) + ((income - 20_000) * 0.2)


print(calculate_tax(45000))