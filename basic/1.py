def sum_or_mul(number1: int, number2: int):
    result = number1 * number2
    return result if result <= 1000 else number1 + number2


# Given Input:

# Case 1: number1 = 20, number2 = 30
# Case 2: number1 = 40, number2 = 30
# Expected Output:

# The result is 600
# The result is 70

print(sum_or_mul(20, 30))
print(sum_or_mul(40, 30))
