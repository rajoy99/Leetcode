class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        list2=list(ransomNote)
        list1=list(magazine)
    
        dic1=collections.Counter(list1)
        
        for i in list2:
            if not dic1[i]:
                return False
            if dic1[i]<list2.count(i):
                return False
            
        return True
        
