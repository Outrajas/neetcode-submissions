
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vis=[]
        prev=None
        curr=head
        while curr:
            if curr in vis:
                return True
            vis.append(curr)    
            curr=curr.next
        return False        

        