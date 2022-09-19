class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result=[]
        
        def backtrack(start,comb,k):
            
            if len(comb)==k:
                result.append(comb.copy())
                
            
            for i in range(start,len(nums)):
                comb.append(nums[i])
                backtrack(i+1,comb,k)
                comb.pop()
        
        for z in range(len(nums)+1):
            backtrack(0,[],z)
        return result