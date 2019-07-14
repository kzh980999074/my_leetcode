'''
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''
def isSymmetric(self, root):

    if not root : return True
        
    stackr=[[],[]]
    stackl=[[],[]]
    i=0
    stackr[i].append(root.right)
    stackl[i].append(root.left)
    while True:
        
        if len(stackr[i%2])==len(stackl[i%2]):
            if not stackr[i%2]:
                break
            while stackr[i%2]:
                r=stackr[i%2].pop()
                l=stackl[i%2].pop()
                if r!=None and l!=None:
                    if r.val==l.val:
                        stackr[(i+1)%2].append(r.left)
                        stackr[(i+1)%2].append(r.right)
                        stackl[(i+1)%2].append(l.right)
                        stackl[(i+1)%2].append(l.left)
                    else:
                        return False
                elif r==None and l==None:
                    pass
                else:
                    return False
            i+=1
        else:
            return False
        return True
    
    