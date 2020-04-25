class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        st=set()
        
        while head:
            if head not in st:
                
                st.add(head)
                head=head.next
            else:
                return True
            
        return False
