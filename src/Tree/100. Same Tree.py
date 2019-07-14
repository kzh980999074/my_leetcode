def isSameTree(p,q):
    stack=[]
    stack.append((p,q))
    while stack:
        
        p,q=stack.pop()
        
        if p!=None and q!=None :
            if p.val==q.val:
                stack.append((p.left,q.left))
                stack.append((p.right,p.right))
            else:
                return False
            
        elif p==None and q==None:
            continue
        
        else :
            return False
        
    return True
 