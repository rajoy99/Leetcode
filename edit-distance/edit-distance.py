class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        word1='*'+word1
        word2='$'+word2
        
        m=len(word1)
        n=len(word2)
        
        dp=[[0 for i in range(m)] for i in range(n)]
        
        for i in range(n):
            dp[i][0]=i
            
        for j in range(m):
            dp[0][j]=j
        
        for i in range(1,n):
            for j in range(1,m):
                if word1[j]==word2[i]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    
        return dp[-1][-1]
        