class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        idx=-1
        
        total=sum(nums)
        
        # res=[0 for i in range(len(nums))]
        # res[0]=nums[0]
        until=0
        
        for i in range(len(nums)):
            if(until==(total-nums[i])/2):
                idx=i
                break
            until+=nums[i]
            
            
            
        return idx
        
        