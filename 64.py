def hollow_triangle(height: int):
    for i in range(0, height + 1):
        if i == 0:
            print("*")
            continue

        if i == height:
            print("*" * i)
            continue

        print("*", end=(" " * (height - 2)))
        print("*")

hollow_triangle(5)
