from ClassTree import Tree, TreeNode, PrintTree


def buildTree1(array, i):
    if i >= len(array):
        return None
    else:
        root = TreeNode(array[i])
        # To the left of the root
        root.left = buildTree1(array, 2*i + 1)
        # To the left of the root
        root.right = buildTree1(array, 2*i + 2)
        return root.data



def childNodes(i):
     return (2*i)+1, (2*i)+2

def buildTree(a, i=0, d = 0):
    if i >= len(a):
        return 
    l, r =  childNodes(i)
    buildTree(a, r, d = d+1)
    print("   "*d + str(a[i]))
    buildTree(a, l, d = d+1)


a = [8, 9, 11, 7, 16, 3, 1]


g = buildTree(a)








