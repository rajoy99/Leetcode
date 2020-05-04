class Solution:
    def findComplement(self, num: int) -> int:
        ans=0
        def intobin(a):
            
            res=[]
            while a>0:
                res.append(a%2)
                a=a//2
            return res[::-1]
        
        res1=intobin(num)
        
        for i in range(len(res1)):
            if res1[i]==1:
                res1[i]=0
            else:
                res1[i]=1
        
        for i in range(len(res1)):
            ans+=res1[::-1][i]*(2**i)
        return ans
            
            
