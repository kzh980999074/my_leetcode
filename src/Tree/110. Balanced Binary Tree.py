'''
Given a binary tree, determine if it is height-balanced.
'''
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
'false'
def isbalanced(root):
    if not root :return True
    l=-1
    i=0
    
    stack=[[],[]]
    stack[0].append(root)
    while stack[i%2]:
        while stack[i%2]:
            p=stack[i%2].pop()
            if p!=None:
                stack[(i+1)%2].append(p.left)
                stack[(i+1)%2].append(p.right)
            else:
                l=i
        if l==i:
            print(l)
            break
        else:
            i+=1
    for j in stack[(i+1)%2]:
        if j!=None:
            if j.right==None and j.left==None:
                continue
            else:
                return False
    return True
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(3)
root.left.left.left=TreeNode(4)
root.left.left.right=TreeNode(4)
print(isbalanced(root))
