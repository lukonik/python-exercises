num = 76542
reverse_number = 0

while num > 0:
    # Get the last digit
    digit = num % 10
    # Add it to the reverse (shifting existing digits left)
    reverse_number = (reverse_number * 10) + digit
    # Remove the last digit from the original number
    num = num // 10

print(reverse_number)