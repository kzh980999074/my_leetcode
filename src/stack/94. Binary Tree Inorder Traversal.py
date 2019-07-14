'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def inorderTraversal(root):
    if not root:return []
    result=[]
    stack=[]
    i=0
    stack.append(root)
    while stack:
        p=stack.pop()
        print(p.val)
        if p.right:
            stack.append(p.right)
            i=0
                
        if p.left:
            if i==2:
                stack.append(p)
                p.left=None
            else:
                stack.append(p)
                stack.append(p.left)
                i=1
        else:
            result.append(p.val)
            i=2 if i==1 else 0
            
    return result
root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)

print(inorderTraversal(root))