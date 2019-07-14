
def maxDepth(root):
    stack=[[],[]]
    if not root: return 0
    i=0
    stack[0].append(root)
    while stack[i%2]:
        while stack[i%2]:
            p=stack[i].pop()
            
            if p!=None:
                if p.left!=None:
                    stack[(i+1)%2].append(p.left)
                if p.right!=None:
                    stack[(i+1)%2].append(p.right)
        i+=1
    
    return i
            