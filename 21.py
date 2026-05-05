def half_pyramid(rows: int):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print("\n")

half_pyramid(5)
