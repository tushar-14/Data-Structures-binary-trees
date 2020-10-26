class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def nthinorder(root,n):
    if not root:
        return

    count=0
    if(count<=n):
        nthinorder(root.left,n)
        count+=1

        if(count==n):
            print("node at pos",n,"is",root.var)

        nthinorder(root.right,n)

root = Node(10)  
root.left = Node(20)  
root.right = Node(30)  
root.left.left = Node(40)  
root.left.right = Node(50)        

n=4
nthinorder(root,n)