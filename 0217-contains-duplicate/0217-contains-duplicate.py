class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        st=set()
        
        for i in nums:
            if i not in st:
                st.add(i)
            else:
                return True
        return False
        