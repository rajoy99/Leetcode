class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        numset=set(nums)
        
        rng=range(1,len(nums)+1)
        res=[]
        
        for i in rng:
            if i not in numset:
                res.append(i)
        return res
                
        