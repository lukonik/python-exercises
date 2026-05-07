def print_reverse_number_pattern(row_number: int):
    for i in range(5, 0, -1):
        print()
        for j in range(i, 0, -1):
            print(j, end=" ")


print_reverse_number_pattern(5)
