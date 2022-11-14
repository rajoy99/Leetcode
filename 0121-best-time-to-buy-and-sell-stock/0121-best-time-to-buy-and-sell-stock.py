class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxsofar=0
        
        l=0
        r=1
        
        while r<len(prices):
            if prices[r]<=prices[l]:
                l=r
            else:
                maxsofar=max(prices[r]-prices[l],maxsofar)
            r+=1
                
        return maxsofar
        