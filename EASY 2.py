class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root

# Function to print the tree in a readable format
def printTree(root):
    if not root:
        return "null"

    left_str = printTree(root.left)
    right_str = printTree(root.right)

    return f"{root.val}, {left_str}, {right_str}".replace(", null, null", "")

# Take input from the user for the sorted array
nums_input = input()
nums = [int(num) if num.lower() != 'null' else None for num in nums_input.split(',')]

# Convert the sorted array to a balanced BST
result = sortedArrayToBST(nums)

# Print the result
print("[",printTree(result),"]")
