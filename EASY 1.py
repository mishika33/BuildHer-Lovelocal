def length_of_last_word(s):
    # Split the input string into a list of words
    words = s.split()

    # Check if there are any words in the list
    if not words:
        # If there are no words, return 0
        return 0

    # Return the length of the last word in the list
    return len(words[-1])


# Get user input
user_input = input()

# Call the function with user input
result = length_of_last_word(user_input)

# Print the result
print(result)
