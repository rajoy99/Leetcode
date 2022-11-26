class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum=-math.inf
        curSum=0
        
        for i in nums:
            curSum+=i
            maxSum=max(curSum,maxSum)
            if curSum<=0:
                curSum=0
            
            
        return maxSum 