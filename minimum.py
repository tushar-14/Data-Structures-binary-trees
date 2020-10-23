class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def treemin(root):
    if not root:
        return float('inf')

    data=root.val
    ln=treemin(root.left)
    rn=treemin(root.right)

    if(ln<rn):
        data=ln
    if(rn<ln):
        data =rn
    return data           