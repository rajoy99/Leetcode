class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cntr=collections.Counter(nums)
        res=[]
        
        tpcntr=list(cntr.items())
        tpcntr=list(sorted(tpcntr,key = lambda x : x[1], reverse = True))
        
        for i in range(k):
            res.append(tpcntr[i][0])
        
         
        
        return res
        