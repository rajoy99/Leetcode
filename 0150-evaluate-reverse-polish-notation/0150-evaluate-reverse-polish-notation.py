class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators=['+','-','*','/']
        stk=[]
        res=0
        
        for i in tokens:
            if i in operators:
                a=int(stk.pop())
                b=int(stk.pop())
                if i=='+':
                    res=(b+a)
                elif i=='-':
                    res=(b-a)
                elif i=='*':
                    res=(b*a)
                elif i=='/':
                    res=(b/a)
                stk.append(res)
            else:
                stk.append(i)
                
        return int(stk[-1])
                    
                
                
        