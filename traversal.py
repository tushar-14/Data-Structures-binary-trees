class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
  
# A function to do inorder tree traversal 
    def printInorder(self,root): 
  
        if root: 
            self.printInorder(root.left) 
            print(root.val, end="-" ) 
            self.printInorder(root.right) 
  
  
  
# A function to do postorder tree traversal 
    def printPostorder(self,root): 
  
        if root:  
            self.printPostorder(root.left)  
            self.printPostorder(root.right) 
            print(root.val, end="-")
  
  
# A function to do preorder tree traversal 
    def printPreorder(self,root): 
  
        if root: 
            print(root.val, end="-")
            self.printPreorder(root.left)
            self.printPreorder(root.right) 
  
  
# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
print ("Preorder traversal of binary tree is")
root.printPreorder(root) 
  
print ("\nInorder traversal of binary tree is")
root.printInorder(root) 
  
print ("\nPostorder traversal of binary tree is")
root.printPostorder(root) 