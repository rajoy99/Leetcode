class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
       
        nums=list(set(nums))
        
        nums.sort()
        
        lc=[1]*len(nums)
        
        count=0
        
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                lc[i]=lc[i-1]+1
                            
        return max(lc)
                
        