class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 


def count_leafnode(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    else:
        return count_leafnode(root.left)+count_leafnode(root.right)     


root = Node(10)  
root.left = Node(20)  
root.right = Node(30)  
root.left.left = Node(40)  
root.left.right = Node(50) 

print("no of leaf node:",count_leafnode(root))