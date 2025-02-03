from ClassTree import Tree, TreeNode, PrintTree

def MinDepth(node):
    if node is None:
        return 0
    else:
        left_depth = MinDepth(node.left)
        right_depth = MinDepth(node.right)

        return min(MinDepth(node.left), MinDepth(node.right)) + 1
    
        
#    // Create the BST
#
#          20
#         /  \
#        10    30
#       / \   / \
#      8   9 23  26
 

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(8)
root.left.right = TreeNode(9)
root.right.left = TreeNode(23)
root.right.right = TreeNode(26)


PrintTree(root)

print(f"\nМинимальная глубина дерева: {MinDepth(root)}\n")


    
