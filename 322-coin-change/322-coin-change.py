class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        dp=[math.inf for i in range(amount+1)]
        
        dp[0]=0
        
        for amnt in range(amount+1):
            for coin in coins:
                if amnt>=coin:
                    dp[amnt]=min(dp[amnt-coin]+1,dp[amnt])
                else:
                    break
                    
        return dp[amount] if dp[amount]<=amount else -1
        