'''
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
import math
from _hashlib import new
def insertionList(head):
    
    if head==None or head.next==None: return head
    
    new=ListNode(-math.inf)
    new.next=head
    head=new
    
    temp=new
    p=new
    
    while p.next!=None:
        
        while temp.next.val<p.next.val:
            temp=temp.next
        if temp != p:
        pp=p.next
        p.next=p.next.next
            
        pp.next=temp.next
        temp.next=pp
        temp=new
    else:
        p=p.next
        temp=new
    return new.next
            
            