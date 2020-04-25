class Solution:
    
    
    def canJump(self, nums: List[int]) -> bool:
        
        m=0
        
        for i in range(len(nums)):
            if i>m:
                return False
            m=max(i+nums[i],m)
        return True


            
                
        
        
        
