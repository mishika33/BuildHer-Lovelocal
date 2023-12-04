def majority_elements(nums):
    if not nums:
        return []

    candidate1, candidate2, count1, count2 = None, None, 0, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    # Use a list to maintain the order of appearance
    appeared_order = []

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        # Store the order of appearance in the list
        if num not in appeared_order:
            appeared_order.append(num)

    result = []
    # Check the count and order of appearance to determine majority elements
    for num in appeared_order:
        if num == candidate1 and count1 > len(nums) // 3:
            result.append(num)
        elif num == candidate2 and count2 > len(nums) // 3:
            result.append(num)

    return result


# Take user input as a comma-separated string of integers
user_input = input()
nums = list(map(int, user_input.split(',')))

# Call the majority_elements function and store the result
result = majority_elements(nums)

# Print the final result
print(result)
