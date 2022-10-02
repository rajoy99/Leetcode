class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators=set(['+','-','*','/'])
        stk=[]
        
        for i in tokens:
            if i not in operators:
                stk.append(i)
            else:
                a=int(stk.pop())
                b=int(stk.pop())
                if i=='+':
                    stk.append(a+b)
                elif i=='-':
                    stk.append(b-a)
                elif i=='*':
                    stk.append(a*b)
                else:
                    stk.append(b/a)
                    
        return int(stk[-1])
        
        