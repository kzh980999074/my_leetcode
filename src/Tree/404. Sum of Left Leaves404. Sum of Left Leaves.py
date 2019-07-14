'''
Created on 2018年8月9日

@author: kai
'''

def sumOfLeftleaves(root):
    if not root:return 0
    stack=[[],[]]
    i=0
    leftsum=0
    stack[i].append(root)
    while stack[i%2]:
        while stack[i%2]:
            p=stack[i%2].pop()
            if p!=None:
                if p.left!=None:
                    if p.left.right==None and p.left.left==None:
                        leftsum+=p.left.val
                    else:
                        stack[(i+1)%2].append(p.left)
                if p.right!=None:
                    stack[(i+1)%2].append(p.right)
        i+=1
    return leftsum

