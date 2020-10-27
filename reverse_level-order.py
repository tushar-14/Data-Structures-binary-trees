from collections import deque

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
def reverse_levelorder(root):
    q = deque()
    q.append(root)
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:
            continue
         
        ans.appendleft(node.data)
         
        if node.right:
            q.append(node.right)
             
        if node.left:
            q.append(node.left)
             
    return ans

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

ans=reverse_levelorder(root)
i=0
print("Level Order traversal of binary tree is")

for i in ans:
    print(i, end=" ")
print("")
