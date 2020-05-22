class Solution:
    def frequencySort(self, s: str) -> str:
        
        cnt=collections.Counter(s)
        
        t=cnt.most_common() # [(,)]
        
        res=''
        for k,v in t:
            for i in range(v):
                res+=k
                
        return res
        
        
