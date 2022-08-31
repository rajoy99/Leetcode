class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hm={}
        st=set()
        
        for i in range(len(s)):
            if s[i] in hm:
                if hm[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in st:
                    return False
                else:
                    hm[s[i]]=t[i]
                    st.add(t[i])
                
        return True
                
            
        