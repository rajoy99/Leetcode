class Solution:
    def intToRoman(self, num: int) -> str:
        
        symbols=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        values=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        
        mapping=dict(zip(values,symbols))
        
        res=''
        idx=len(values)-1
        
        while num>0 and idx>=0:
            if num//values[idx]>0:
                res+=mapping[values[idx]]
                num=num-values[idx]
            else:
                idx-=1
                
        return res
            
            
        
        