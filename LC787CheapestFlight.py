class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        costs=[math.inf]*n
        costs[src]=0
        
        
        for _ in range(K+1):
            copy=costs[:]
            
            for u,v,w in flights:
                copy[v]=min(copy[v],costs[u]+w)
            costs=copy
        return costs[dst] if costs[dst]!=math.inf else -1
        
        
        
        
