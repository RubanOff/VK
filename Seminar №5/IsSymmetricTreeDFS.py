from ClassTree import Tree, TreeNode, PrintTree

# DFS!!

def deptSearch(root, res):

    if root == None:
        return
    
    deptSearch(root.left, res)
    res.append(root.data)
    deptSearch(root.right, res)


def isSymmetricTreeDFS(root):
    if root == None:
        return True
    
    data =[]
    deptSearch(root, data)
    j = len(data) - 1

    for i in range(round(len(data)/2)):
        if data[i] != data[j]:
            return False
        j -= 1

    return True


# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.right.right = TreeNode(4)

PrintTree(root)

print(f"\nIs symmetric tree?: {isSymmetricTreeDFS(root)}\n")
