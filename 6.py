def addition(num: int):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return addition(num-1) + addition(num - 2)


print(addition(10))