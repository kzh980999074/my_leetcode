'''
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
return c1
len(a+c)
len(b+c)
len(a+b)
'''
from builtins import None

def getIntersectionNode(headA,headB):
        if headA==None or headB==None:
            return None
        
        pa=headA
        pb=headB
        while pa.next!=None:
            pa=pa.next
        while pb.next!=None:
            pb=pb.next
        
        if pa!=pb:
            return None
        
        pa=headA
        pb=headB

        while pa != pb:
            pa = headB if pa==None else pa.next
            pb = headA if pb==None else pb.next

        return pa

    
    
    