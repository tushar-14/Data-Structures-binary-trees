class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left) 
    print(temp.val,end = " ")
    inorder(temp.right) 

def mirror(root):
    if not root:
        return
    else:
        temp=root

        mirror(root.left)
        mirror(root.right)
#swap the pointers in this node
        temp=root.left
        root.left=root.right
        root.right=temp



root =Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)  
  
""" Print inorder traversal of 
        the input tree """
print("Inorder traversal of the constructed tree is")  
inorder(root)  
      
""" Convert tree to its mirror """
mirror(root)  
  
""" Print inorder traversal of  
        the mirror tree """
print("\nInorder traversal of the mirror tree is ")  
inorder(root)        
