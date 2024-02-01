#this is a red-black tree implementation

class TreeNode:
    def __init__(self, val=0, color='b', parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.color = color
        self.parent = parent

    def left_rotate(self, root):
        x, y = root, root.right
        if not y: return False
        a, b, c = x.left, y.left, y.right
        y.left = x
        x.right = b
        return y
    
    def right_rotate(self, root):
        x, y = root, root.left
        if not y: return False
        a, b, c = y.left, y.right, x.right
        y.right = x
        x.left = b
        return y
        

class RedBlackTree:
    def __init__(self, root=None):
        self.root = root

    def search(self, val: int):
        pass

    def insert(self, val: int):   
        # base case, root mush be black
        if not self.root:
            self.root = TreeNode(val)
            return
        
        def dfs(node):
            if node.val<val: 
                if not node.right: return node, 'r'
                return dfs(node.right)
            elif node.val>val:
                if not node.left: return node, 'l'
                return dfs(node.left)
        
        # insert the node as normal, try coloring it red
        y, dir = dfs(self.root)
        if dir=='l': 
            y.left = TreeNode(val, 'r', y)
        else: 
            y.right = TreeNode(val, 'r', y)
        # y is black, done
        if y.color=='b': return

        # y is red, then trace y's parent w, which must be black
        w = y.parent
        # TODO: case 1: w's other child is red