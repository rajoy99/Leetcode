 #LC  20 valid parentheses
 class Solution:
    def isValid(self, s: str) -> bool:
        
        stk=[]
        for i in s:
            g=len(stk)
            
            if (i==')' and g==0)or(i=='}'and g==0)or(i==']'and g==0):
                return False
            elif (i==')' and stk[-1]=='(') or(i=='}'and stk[-1]=='{') or(i==']' and stk[-1]=='['):
                stk.pop()
            else:
                stk.append(i)
            
            
        return len(stk)==0