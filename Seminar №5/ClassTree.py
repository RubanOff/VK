
# Class TreeNode 
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# To work with binary tree
class Tree:
    def __init__(self):
        self.root = None

    # Method "__find" which find the necessary node
    def __find(self, node, parent, value):

        # Check that node is None
        if node is None:
            return None, parent, False

        # Chech that value equal data
        if value == node.data:
            return node, parent, True
        
        # Left search
        if value < node.data:
            # Is exist left node?
            if node.left:
                return self.__find(node.left, node, value)
            
        # Right search 
        if value > node.data:
            # Is exist right node?    
            if node.right:
                return self.__find(node.right, node, value)
            
        return node, parent, False
    
    def show_wide_tree(self, node):
        if node is None:
            return 
        
        # Peaks for the current level
        v = [node]
        while v:
            v_new = []
            for i in v:
                print(i.data, end= "  ")
                if i.left:
                    v_new += [i.left]
                if i.right:
                    v_new += [i.right]
            print()
            
            v = v_new


    # Method append which add an array/number into binary tree
    def append(self, obj):
        # If root is ubsent: assign number to root
        if self.root is None:
            self.root = obj
            return obj

        s, p, flag_find = self.__find(self.root, None, obj.data)

        if not flag_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj
    

    # Delete node without child
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None


    # Delete node with one child
    def __del_one_child(self, s, p):

        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left
            

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        
        return node, parent
    
    
    # Delete a node
    def del_node(self, key):

        s, p, flag_find = self.__find(self.root, None, key)


        if flag_find == False:
            return None
        
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    
    def show_tree(self, node):
        if node is None:
            return None
        
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

def PrintTree(node, level=0):
    if node is not None:
        PrintTree(node.right, level + 1)
        print('    ' * level + str(node.data))
        PrintTree(node.left, level + 1)



def childNodes(i):
     return (2*i)+1, (2*i)+2

def buildTree(a, i=0, d = 0):
    if i >= len(a):
        return 
    l, r =  childNodes(i)
    buildTree(a, r, d = d+1)
    print("   "*d + str(a[i]))
    buildTree(a, l, d = d+1)







# t = Tree()
# h = [3, 8, 8, 9, 6, 6, 9]

# for x in h:
#     t.append(TreeNode(x))

# g = t.show_tree(t.root)


# print(isSymmetricTreeDFS(t.root))

# buildTree(h)

#############