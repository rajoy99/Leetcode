class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        res=[]
        todo=collections.defaultdict(set)
        graph=collections.defaultdict(set)
        
        for i,j in prerequisites:
            todo[i].add(j)
            graph[j].add(i)
        stk=[i for i in range(numCourses) if not todo[i]]
        
        while stk:
            a=stk.pop()
            res.append(a)
            for i in graph[a]:
                todo[i].remove(a)
                if not todo[i]:
                    stk.append(i)
                    
        if len(res)==numCourses:
            return True
        else:
            return False
