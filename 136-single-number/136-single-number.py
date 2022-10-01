class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res=nums[0]
        
        for v in nums[1:]:
            res=res^v
            
        return res
        