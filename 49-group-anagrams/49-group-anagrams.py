class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap=defaultdict(list)
        
        for i in strs:
            s_l=list(i)
            s_l.sort()
            s_l=tuple(s_l)
            hmap[s_l].append(i)
            
            
           
        res=[]
        
        for k,v in hmap.items():
            ans=[]
            for i in v:
                ans.append(i)
            res.append(ans)
            
        return res
                
        