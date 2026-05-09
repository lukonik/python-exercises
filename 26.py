def sort_emplyoes(data: list[tuple[str, int, int]]):
    return sorted(data, key=lambda data: data[2], reverse=False)


employees = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]

print(sort_emplyoes(employees))
