def function():
    prev_number = 0
    sum = 0
    for value in range(9):
        sum += value
        print(f"Curr: {value}, Prev: {prev_number}, Sum: {sum}")
        prev_number = value

# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number 0 Sum: 0
# Current Number 1 Previous Number 0 Sum: 1
# Current Number 2 Previous Number 1 Sum: 3
# ....
# Current Number 8 Previous Number 7 Sum: 15
# Current Number 9 Previous Number 8 Sum: 17

function()