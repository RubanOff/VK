from ClassTree import Tree, TreeNode, PrintTree

def isSameTree(a, b):

    if a == None and b == None:
        return True
    if a == None or b == None:
        return False
    if a.data != b.data:
        return False
    
    return isSameTree(a.left, b.left) and isSameTree( a.right, b.right)



# Tests
# First tree
a = TreeNode(20)
a.left = TreeNode(10)
a.right = TreeNode(30)
a.left.left = TreeNode(8)
a.left.right = TreeNode(9)
a.right.left = TreeNode(23)
a.right.right = TreeNode(26)

# Second tree
b = TreeNode(20)
b.left = TreeNode(10)
b.right = TreeNode(30)
b.left.left = TreeNode(8)
b.left.right = TreeNode(9)
b.right.left = TreeNode(23)
b.right.right = TreeNode(26)


print(f"\nAre the trees the same: {isSameTree(a, b)}\n")




