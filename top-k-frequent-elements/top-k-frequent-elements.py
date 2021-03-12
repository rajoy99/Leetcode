class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt=collections.Counter(nums)
        cnt=dict(cnt)
        new={ke:v for ke,v in sorted(cnt.items(),key=lambda item: item[1],reverse=True)}
        
        res=[]
        for key,v in new.items():
            res.append(key)
            
        return res[:k]
        
        