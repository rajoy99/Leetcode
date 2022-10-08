class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph={i:[] for i in range(1,n+1)}
        
        for u,v,w in times:
            graph[u].append((w,v))
        
        minHeap=[(0,k)] # cost,node
        dist={}
        visited=set()
        
        
        while minHeap:
            cost,node=heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            dist[node]=cost
            for neighcost,neigh in graph[node]:
                if neigh not in visited:
                    heapq.heappush(minHeap,(neighcost+cost,neigh))
   
             
           
        return max(dist.values()) if len(visited)==n else -1
            
        