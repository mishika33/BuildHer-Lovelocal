def maxSlidingWindow(nums, k):
    if not nums:
        return []

    result = []
    window = []

    for i in range(len(nums)):
        # Remove elements outside the current window
        while window and window[0] < i - k + 1:
            window.pop(0)

        # Remove smaller elements as they won't be needed
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)

        # Add maximum element to result for each valid window
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Get user input for the array nums
user_input_nums = input()
nums = [int(num) for num in user_input_nums.split(',')]

# Get user input for the window size k
k = int(input())

# Call the function with user input
result = maxSlidingWindow(nums, k)

# Display the result
print(result)
