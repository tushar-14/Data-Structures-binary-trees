class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def countnode(root):
    if not root:
        return 0
    return 1+countnode(root.left)+countnode(root.right)

root = Node(10)  
root.left = Node(20)  
root.right = Node(30)  
root.left.left = Node(40)  
root.left.right = Node(50) 

print("no of nodes are:",countnode(root))
