class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        s=[v for v in s if 97<=ord(v)<=122 or 48<=ord(v)<58]
        
        print(s)
        return s==s[::-1]
        