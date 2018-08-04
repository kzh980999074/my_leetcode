#Input: 1->2->3->4->5->NULL, m = 2, n = 4
#Output: 1->4->3->2->5->NULL

def reverseBetween(self, head, m, n):
	if m>=n:return head
    new=ListNode(0)
	new.next=head
	head=new
        
	count=1
	p=head
        
	while count<m:
		p=p.next
		count+=1
        
	p1=p.next
	while count<n:
		pp=p1.next
		p1.next=p1.next.next
		pp.next=p.next
		p.next=pp
		count+=1
        
	return new.next