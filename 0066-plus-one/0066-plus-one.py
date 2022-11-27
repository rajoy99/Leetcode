class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res=[]

        i=len(digits)-1
        c=True
        while i>=0:
            if c:
                summation=digits[i]+1
            else:
                summation=digits[i]
                
            if summation>=10:
                res.append(summation%10)
                c=True
            else:
                res.append(summation)
                c=False
            i-=1
        
        return res[::-1] if c==False else [1]+res[::-1]
            
        