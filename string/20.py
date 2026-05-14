str1 = "PYnative29@#8496"

only_digits=[int(digit) for digit in str1 if digit.isdigit()]


print(f"Sum is: {sum(only_digits)}, Average: {sum(only_digits)/len(only_digits):.2f}")