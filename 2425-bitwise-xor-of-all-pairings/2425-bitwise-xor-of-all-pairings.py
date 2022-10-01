class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums3=[]
        
        for i in nums1:
            if len(nums2)%2:
                nums3.append(i)
                
        for i in nums2:
            if len(nums1)%2:
                nums3.append(i)

        res=0
        
        for v in nums3:
            res^=v
            
        return res
