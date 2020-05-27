class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        graph=collections.defaultdict(set)
        
        
        for a,b in dislikes:
            graph[a].add(b)
            graph[b].add(a)
        
        seen={}
        
        def check(start):
            q=[(start,1)]
            
            while q:
                a,color=q.pop()
                if a in seen:
                    if seen[a]!=color:
                        return False
                    continue
                seen[a]=color
                
                for v in graph[a]:
                    q.append((v,-color))
            return True
        
        for i in range(1,N+1):
            if i not in seen and not check(i):
                return False
            
        return True
        
        
