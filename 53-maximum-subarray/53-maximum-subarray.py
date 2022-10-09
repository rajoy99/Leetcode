class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        maxsofar=-math.inf
        curSum=0
        
        for i in nums:
            curSum+=i
            maxsofar=max(curSum,maxsofar)
            if curSum<0:
                curSum=0
                
                
        return maxsofar