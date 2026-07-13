class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        l=0
        while curr:
            l=l+1
            curr=curr.next   
        if l==1 or l==0:
            return None     
        i=0    
        
        jump=head
        prev=None
        while jump:
            if i==l-n:
                if prev:
                    prev.next=jump.next
                else:   
                    head=jump.next
                return head    
            i+=1    
            prev=jump    
            jump=jump.next
            



            



        