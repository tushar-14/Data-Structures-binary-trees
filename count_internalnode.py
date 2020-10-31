class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 


def count_internalnode(root):
    if not root:
        return 0
    if not root.right and not root.left:
        return 0    

    return 1+ count_internalnode(root.right) + count_internalnode(root.left)    

root = Node(10)  
root.left = Node(20)  
root.right = Node(30)  
root.left.left = Node(40)  
root.left.right = Node(50) 

print("no of internal nodes:",count_internalnode(root))