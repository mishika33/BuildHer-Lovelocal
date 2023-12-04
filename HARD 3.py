def count_digit_one(n):
    
    count = 0

    # Iterate through each number from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Convert the current number to its decimal representation as a string
        number_str = str(i)

        # Count the occurrences of the digit '1' in the decimal representation
        one_count = number_str.count('1')

        # Add the count for the current number to the overall count
        count += one_count

    # Return the total count of digit '1' occurrences
    return count

# Take input from the user for the integer n
user_input = int(input())

# Call the function with user input
result = count_digit_one(user_input)
print(result)
