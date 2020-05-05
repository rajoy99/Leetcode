class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph=collections.defaultdict(list)
        
        for u,v,w in times:
            graph[u].append((w,v))
        
        pq=[(0,K)] #The starting node
        dist={}    #a dict to keep track
        
        while pq:
            d,node=heapq.heappop(pq)
            if node in dist:
                continue
            dist[node]=d #update the distance
            for d2,nei in graph[node]:
                if nei not in dist: # Check if the node is in dist
                    heapq.heappush(pq,(d+d2,nei))
        return max(dist.values()) if len(dist)==N else -1
