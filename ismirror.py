class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key

def isidentical(root1,root2):
    if not root1 and not root2:
        return True

    if root1 and root2:
        return root1.data==root2.data and isidentical(root1.left,root2.right) and isidentical(root1.right,root2.left)
    return False



root1 = Node(1)  
root1.left = Node(2)  
root1.right = Node(3)  
root1.left.left = Node(4)  
root1.left.right = Node(5)    

root2 = Node(1)  
root2.left = Node(2)  
root2.right = Node(3)  
root2.left.left = Node(4)  
root2.left.right = Node(5)

print("Are trees mirror ?",isidentical(root1,root2))