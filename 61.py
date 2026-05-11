def generate_pascal(n):
    triangle = [[1]]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        # Start the row with 1
        new_row = [1]
        
        # Calculate the middle elements
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        # End the row with 1
        new_row.append(1)
        triangle.append(new_row)
        
    return triangle

# Usage
for row in generate_pascal(5):
    print(row)