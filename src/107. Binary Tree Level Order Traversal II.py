'''
    3
   / \
  9  20
    /  \
   15   7

[
  [15,7],
  [9,20],
  [3]
]

'''
def levelOrderBottom(root):
    if not root:
        return []
    temp=[]
    stack=[[],[]]
    i=0
    stack[i].append(root)
    while stack[i%2]:
        l=[]
        while stack[i%2]:
            p=stack[i%2].pop()
            if p!=None:
                l.append(p.val)
                stack[(i+1)%2].append(p.left)
                stack[(i+1)%2].append(p.right)
        if l:
            temp.append(l)
    temp.reverse()
    return temp
            