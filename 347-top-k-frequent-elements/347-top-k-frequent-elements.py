class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt=Counter(nums)
        
        
        li=[(k,v) for k,v in cnt.items()]
        
        li.sort(key= lambda x: x[1], reverse = True)
        
        return [i for i,j in li[:k]]