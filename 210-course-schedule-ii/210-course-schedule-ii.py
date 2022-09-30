class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        dependence=defaultdict(set)
        graph=defaultdict(set)
        
        canDo=[]
        
        for a,b in prerequisites:
            graph[b].add(a)
            dependence[a].add(b)
            
        
        stk=[i for i in range(numCourses) if not dependence[i]]

        
        while stk:
            
            node=stk.pop()
            canDo.append(node)
            
            for neigh in graph[node]:
                dependence[neigh].remove(node)
                if not dependence[neigh]:
                    stk.append(neigh)
                    
            
                    
                
     
        return canDo if len(canDo)==numCourses else []
        