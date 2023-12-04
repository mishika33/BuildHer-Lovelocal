class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    # Ensure p is smaller than q
    if p.val > q.val:
        p, q = q, p

    while root:
        # If the current node value is greater than q, move to the left subtree
        if root.val > q.val:
            root = root.left
        # If the current node value is smaller than p, move to the right subtree
        elif root.val < p.val:
            root = root.right
        # If the current node value is between p and q, or equal to one of them, it is the LCA
        else:
            return root

# Function to build a BST from a list of values
def buildBST(values):
    if not values:
        return None

    root = TreeNode(values[0] if values[0] is not None else None)
    for value in values[1:]:
        insertNode(root, value)

    return root

# Helper function to insert a value into the BST
def insertNode(root, value):
    if value is None:
        return None
    if not root:
        return TreeNode(value)
    if value < root.val:
        root.left = insertNode(root.left, value)
    elif value > root.val:
        root.right = insertNode(root.right, value)
    return root

# Take input from the user for BST values
bst_values = input()
bst_values = [int(val) if val.lower() != 'null' else None for val in bst_values.split(',')]

# Take input from the user for the values of nodes p and q
p_value = int(input())
q_value = int(input())

# Build the BST
root = buildBST(bst_values)
p_node = TreeNode(p_value)
q_node = TreeNode(q_value)

# Find the lowest common ancestor
result = lowestCommonAncestor(root, p_node, q_node)
print(result.val if result else None)
