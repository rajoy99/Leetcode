class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm={}
        
        for i,v in enumerate(nums):
            if v in hm:
                return [hm[v],i]
            else:
                hm[target-v]=i
                
        
        