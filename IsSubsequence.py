# One solution 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        count=0
        j=0
        
        for i in range(len(s)):
            while j<len(t):
                if s[i]==t[j]:
                    count+=1
                    j+=1
                    break
                j+=1
                

                
        
        return count==len(s)
      
                
       
 # Another solution .(Two pointer approach ) 
 class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        i=j=0
        
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            
            if i==len(s):
                return True
            j+=1
        
        return i==len(s)
        
