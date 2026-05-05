def reverse_int(value: int):
    output = ""
    while value > 0:
        module = value % 10
        value = value // 10
        output += str(module)
    return output


# 7536
print(reverse_int(7536))