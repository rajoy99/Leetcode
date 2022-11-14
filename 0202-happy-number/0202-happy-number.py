class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen=set()
        
        while n!=1:
            lst=[int(v) for v in str(n)]
            summation=sum([v**2 for v in lst])
            if summation not in seen:
                seen.add(summation)
            else:
                return False
            n=summation
            
        return True
        