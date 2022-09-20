class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        comb=[0 for i in range(amount+1)]
        
        comb[0]=1
        
        for coin in coins:
            for i in range(amount+1):
                if coin<=i:
                    comb[i]+=comb[i-coin]
                    
        return comb[amount]
        