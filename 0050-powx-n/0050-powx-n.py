class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x,n):
            if x==0: return 0
            if n==1: return x
            if n==0: return 1
            
            res=helper(x,n//2)
            res=res*res
            return res if n%2==0 else res*x
            
        return helper(x,abs(n)) if n>0 else 1/helper(x,abs(n))