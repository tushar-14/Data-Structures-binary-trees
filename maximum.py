class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def treemax(root):
    if not root:
        return float('-inf')

    data=root.val
    ln=treemax(root.left)
    rn=treemax(root.right)

    if(ln>rn):
        data=ln
    if(rn>ln):
        data =rn
    return data           