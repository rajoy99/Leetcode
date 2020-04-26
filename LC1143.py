class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m=len(text1)
        n=len(text2)
        
        dp=[[0 for i in range(n+1)]for i in range(m+1)]
        
        # The trick is to add an whitespace at the beginning
        
        text1=" "+text1
        text2=" "+text2
        
        #Remember to start the Loop from 1
        # As the table consists 1 row and column of 0s
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i]==text2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]
        
                
