class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        dp=[math.inf for i in range(amount+1)]
        dp[0]=0
        
        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i]=min(1+dp[i-coin],dp[i])
                    
        return dp[amount] if dp[amount]<=amount else -1
        
