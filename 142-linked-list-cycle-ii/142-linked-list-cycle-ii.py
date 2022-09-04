# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hset=set()
        i=0
        while head:
            if head in hset:
                return head
            else:
                hset.add(head)
                head=head.next
            i+=1
            
        return None
            
            
        