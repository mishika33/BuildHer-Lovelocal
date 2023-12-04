def shortestPalindrome(s):
    # Helper function to check if a string is a palindrome
    def is_palindrome(string):
        return string == string[::-1]

    n = len(s)
    
    # Find the longest palindrome suffix
    i = n
    while i > 0 and not is_palindrome(s[:i]):
        i -= 1

    # Add the reverse of the remaining prefix to the original string
    return s[i:][::-1] + s

# Take input from the user for the string
user_input = input()
result = shortestPalindrome(user_input)
print(result)
