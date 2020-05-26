class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        firstoccurence={0:-1}
        maxlength=0
        
        sum=0
        for i,v in enumerate(nums):
            if v==1:
                sum+=1
            else:
                sum-=1
            if sum in firstoccurence:
                maxlength=max(maxlength,i-firstoccurence[sum])
            else:
                firstoccurence[sum]=i
            
        return maxlength
                
            
