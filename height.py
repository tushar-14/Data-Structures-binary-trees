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

def height(root):
    if not root:
        return 0

    ldepth=height(root.left)
    rdepth=height(root.right)


    if rdepth > ldepth:
        return rdepth+1
    else:
        return ldepth+1       

# Driver program to test above function 
root = Node(3) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.right.left = Node(4)
root.right.right=Node(6)
root.right.right.right=Node(7)

  
  
print ("Height of tree is %d" %(height(root)))         