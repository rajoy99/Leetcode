class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num)==k:
            return '0'
        res=[]
        
        
        for char in num:
            while k and res and res[-1]>char:
                res.pop()
                k-=1
            res.append(char)
        
        while k:
            k-=1
            res.pop()
        
        return ''.join(res).lstrip('0') or '0'
