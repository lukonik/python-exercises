def show_employee(name: str, salary: int = 9000):
    return f"Name: {name}, Salary: {salary}"


print(show_employee("Ben"))
print(show_employee("Jessa", 12000))
