class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        
        m,n=len(grid),len(grid[0])
        
        if m==1 and n==1:
            return grid[0][0]
        
        dp=[[0 for i in range(n)]for i in range(m)]
        
        dp[0][0]=grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i==0:
                    dp[0][j]=dp[0][j-1]+grid[0][j]
                elif j==0:
                    dp[i][0]=dp[i-1][0]+grid[i][0]
                    
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
                    
                    
        return dp[-1][-1]
        