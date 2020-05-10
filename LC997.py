class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        todo=collections.defaultdict(set)
        
        for u,v in trust:
            todo[u].add(v)
        
        can=0
        rt=0
        for i in range(1,N+1):
            if not todo[i]:
                can=i
                rt+=1
        if rt>1:return -1
                
        if can==0:
            return -1
        todo.pop(can)
             
        for k,v in todo.items():
            if can not in v:
                return -1
            
                
        return can
        

        
