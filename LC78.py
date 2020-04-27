class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[[]]
        
        for e in nums:
            sz=len(res)
            for i in range(sz):
                
                cur=res[i]
                new=cur+[e]
                res.append(new)
        return res
            
        
        
