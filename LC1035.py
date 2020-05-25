class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        dp=[[0 for i in range(len(B)+1)]for i in range(len(A)+1)]
          
        A=[-1]+A
        B=[-1]+B
        
        for i in range(1,len(A)):
            for j in range(1,len(B)):
                if A[i]==B[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]
        
