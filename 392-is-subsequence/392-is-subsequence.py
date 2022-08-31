class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        secidx=0
        i=0 
        count=0
        
        while i<len(s) and secidx<len(t):
            if s[i]==t[secidx]:
                count+=1
                i+=1
                
            secidx+=1
        
        return count==len(s)
            
                
        