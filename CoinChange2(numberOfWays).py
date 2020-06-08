class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        combination=[0 for i in range(amount+1)]
        
        combination[0]=1
        for coin in coins:
            for i in range(1,amount+1):
                if coin<=i:
                    combination[i]+=combination[i-coin]
                
        
        
        return combination[-1]
        
