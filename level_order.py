from collections import deque

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
 

def printlevel_order(root):
    if not root:
        return

    if root.left==None and root.right==None:
        return print(root.data)

    q=deque()
    q.append(root)

    while(len(q)):
        temp=q.popleft()
        print(temp.data, end=" ")

        if temp.left:
            q.append(temp.left)
    
        if temp.right:
            q.append(temp.right)


#Driver Program to test above function  
root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)  
  
print ("Level Order Traversal of binary tree is -")  
printlevel_order(root)  