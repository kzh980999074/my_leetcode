class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


def partition(head,x):
    
    if head==None or head.next==None:return head
    
    p=None
    p0=head
    if head.val>=x:
        while p0.next !=None:
            if p0.next.val<x:
                pp=p0.next
                p0.next=p0.next.next
                pp.next=head
                head=pp
                break
            else:
                p0=p0.next
    if p0==None :return head
    
    p0=head
    p1=head
    while p1.next!=None:
        if p1.next.val<x:
            if p0==p1:
                p0=p0.next
                p1=p0
            else:
                pp=p1.next
                p1.next=p1.next.next
                pp.next=p0.next
                p0.next=pp
                p0=pp
        else:
            p1=p1.next
    return head
            
    
    