class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis=[1]*len(nums)
        
        
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    if lis[i]<=lis[j]:
                        lis[i]+=1
                        
                    
            
                

                
        return max(lis)
            
        