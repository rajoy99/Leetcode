class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        
        dp=[[0 for i in range(n+1)]for i in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j],dp[i][j])+1
                    
        mx=0
        for i in dp:
            for e in i:
                mx=max(e,mx)
        return mx*mx
                
                
        
