class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping={'(':')','{':'}','[':']'}
        
        stk=[]
        
        for i in s:
            if i in mapping:
                stk.append(i)
            elif stk:
                if mapping[stk[-1]]==i:
                    stk.pop()
                else:
                    return False
            else:
                return False
                
        return not stk
                    