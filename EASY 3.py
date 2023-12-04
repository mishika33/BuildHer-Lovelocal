def generate_pascals_triangle(numRows):
    triangle = []

    for i in range(numRows):
        row = [None for _ in range(i + 1)]  # Initialize the row with None values
        row[0], row[-1] = 1, 1  # Set the first and last elements to 1

        # Fill in the rest of the row
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

# Get user input for the number of rows
numRows = int(input())

# Call the function with user input
result = generate_pascals_triangle(numRows)

# Display the result
print(result)
