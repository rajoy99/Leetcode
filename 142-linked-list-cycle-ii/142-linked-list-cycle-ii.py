# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hmap={} # node : position 
        i=0
        while head:
            if head in hmap:
                return hmap[head]
            else:
                hmap[head]=head
                head=head.next
            i+=1
            
        return None
            
            
        