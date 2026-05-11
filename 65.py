def print_diamond(n):
    # Top Half (Growth)
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    
    # Bottom Half (Shrink)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

print_diamond(4)