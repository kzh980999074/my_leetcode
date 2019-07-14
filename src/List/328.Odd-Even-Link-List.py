#Input: 1->2->3->4->5->NULL
#Output: 1->3->5->2->4->NULL
def oddEvenList(head):
    
    if head==None or head.next==None:
        return head
    p0=head
    p1=head.next
    while p1.next!=None:
        p0.next=p1.next
        p0=p0.next
        
        if p0.next !=None:
            p1.next=p0.next
            p1=p1.next
    return head    