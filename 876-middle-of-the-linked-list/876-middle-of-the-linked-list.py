# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        count=0
        
        pointer=head
        
        while head:
            
            count+=1
            head=head.next
            
        count=math.floor(count/2)
        i=0
        while i<count:
            pointer=pointer.next
            i+=1
            
        
        return pointer