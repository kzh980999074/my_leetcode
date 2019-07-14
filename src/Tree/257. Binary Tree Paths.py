'''
Given a binary tree, return all root-to-leaf paths.
   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
'''
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None
        

def binaryTreePaths(root):
    paths=[]
    if not root:return paths
    s=''
    
    def treePath(roots,s=''):
        
        if roots!=None:
            ss=s+str(roots.val)
        if roots.right==None and roots.left==None:
            paths.append(ss)
            return
            
        else:
            if roots.left!=None:
                treePath(roots.left,ss+'->')
            if roots.right!=None:
                treePath(roots.right,ss+'->')
    treePath(root,s='')
    return paths
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(5)
print(binaryTreePaths(root))
