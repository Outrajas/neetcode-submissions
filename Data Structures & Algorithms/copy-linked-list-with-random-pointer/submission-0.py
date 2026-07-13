
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        
        old_to_new = {}
        comp = head
        while comp:
            old_to_new[comp] = Node(comp.val)
            comp = comp.next
        
        comp = head
        while comp:
            old_to_new[comp].next = old_to_new.get(comp.next)
            old_to_new[comp].random = old_to_new.get(comp.random)
            comp = comp.next
        
        return old_to_new[head]
        