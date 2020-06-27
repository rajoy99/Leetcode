class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        self.helper(res,'',n,n)
        return res
    
    def helper(self,res,cur,left,right):
        
        if left<0 or left>right:
            return 
        
        if left==0 and right==0:
            res.append(cur)
            return 
        
        self.helper(res,cur+"(",left-1,right)
        self.helper(res,cur+")",left,right-1)
