class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N=len(points)
        
        graph={i:[] for i in range(N)}
        
        for i in range(N-1):
            x1,y1=points[i]
            for j in range(i+1,N):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                graph[i].append((dist,j))
                graph[j].append((dist,i))
                
                
        res=0
        visited=set()
        minHeap=[(0,0)]
        
        while len(visited)<N:
            
            cost,node=heapq.heappop(minHeap)
            if node in visited:
                continue
            res+=cost
            visited.add(node)
            
            for neighCost,neigh in graph[node]:
                    heapq.heappush(minHeap,(neighCost,neigh))
                    
        return res
            
            
        
                
                
        