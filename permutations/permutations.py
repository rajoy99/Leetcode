class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==1:
            return [nums]
        
        res=[]
        for i in range(len(nums)):
            others=nums[:i]+nums[i+1:]
            other_permutation=self.permute(others)
            
            
            for j in range(len(other_permutation)):
                res.append([nums[i]]+other_permutation[j])
                
                
        return res
                