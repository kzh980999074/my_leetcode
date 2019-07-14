def invertTree(root):
    if not root:return root
    stack=[[],[]]
    stack[0].append(root)
    i=0
    while stack[i%2]:
        while stack[i%2]:
            p=stack[i%2].pop()
            if p!=None:
                q=p.left
                p.left=p.right
                p.right=q
                stack[(i+1)%2].append(p.left)
                stack[(i+1)%2].append(p.right)
        i+=1
    return root