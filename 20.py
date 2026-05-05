def print_table(range_number: int):
    output = ""
    for i in range(1, range_number):
        output += "\n"
        for j in range(1, range_number):
            output += f"{i * j} "
    return output


print(print_table(10))
