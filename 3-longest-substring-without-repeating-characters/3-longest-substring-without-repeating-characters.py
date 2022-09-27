class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=0
        res=0
        cSet=set()
        
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l+=1
            cSet.add(s[r])
            res=max(res,len(cSet))
            
        return res
        
        
        
        