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

def insert(temp,key):
    
    if not root:
        return
    q=[]
    q.append(temp)

    while(len(q)):
        temp=q[0]
        q.pop(0)

        if not temp.left:
            temp.left=Node(key)
            return
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right=Node(key)
            return
        else:
            q.append(temp.right)    

# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 

print("Inorder traversal before insertion:", end = " ")
inorder(root) 
 
key = 8
insert(root, key) 
 
print() 
print("Inorder traversal after insertion:", end = " ")
inorder(root)