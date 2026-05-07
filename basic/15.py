def print_pattern(number_range):
    # Create a list where each item is a formatted string for one row
    output = [" ".join([str(i + 1)] * (i + 1)) for i in range(number_range)]
    
    # Join those rows with a newline character
    all_output = "\n".join(output)
    print(all_output)

print_pattern(5)