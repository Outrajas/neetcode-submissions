class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        num1=[]
        num2=[]
        while curr1 or curr2:
            if not curr1:
                num2.append(curr2.val)
                curr2=curr2.next
                continue
            if not curr2:
                num1.append(curr1.val)
                curr1=curr1.next 
                continue 
            num2.append(curr2.val)
            num1.append(curr1.val)
            curr2=curr2.next 
            curr1=curr1.next   
        add=int("".join(map(str, num1[::-1])))+int("".join(map(str, num2[::-1])))
        add=list(map(int, str(add)[::]))
        dummy=ListNode(0) 
        curr=dummy
        while len(add)!=0:
            curr.next=ListNode(add[-1]) 
            add.pop()
            curr=curr.next
        head=dummy.next
        return head     




