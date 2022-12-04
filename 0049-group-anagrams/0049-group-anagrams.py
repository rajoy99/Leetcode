class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm=collections.defaultdict(list)
        
        for i in strs:

            hm[tuple(sorted(i))].append(i)
            
        res=[]
        
        for k,v in hm.items():
            res.append(v)
        
        return res

        