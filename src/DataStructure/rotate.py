#tree
class Tree:
    def __init__(self):
        self.nil=None
        self.root=None
class TreeNode:
    def __init__(self,x,T):
        self.val=x
        self.T=T
        self.left=T.nil
        self.right=T.nil
        self.p=None
        self.color='R'
def left_rotate(x):
    y=x.right#y代表x的有孩子
    
    x.right=y.left
    if y.left!=x.T.nil:
        y.left.p=x
    
    if x==x.T.root:
        x.T.root=y
    elif x==x.p.left:
        x.p.left=y
    else:
        x.p.right=y
    y.p=x.p
    x.p=y
    






