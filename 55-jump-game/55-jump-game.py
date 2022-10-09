class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums or len(nums)==1:
            return True
        
        goal=len(nums)-1
        left=goal-1
        
        while left>=0:
            print("Goal,l,item : ",goal,left,nums[left])
            if left+nums[left]>=goal:
                goal=left
            left=left-1
            
        
        return goal==0
        
        
        