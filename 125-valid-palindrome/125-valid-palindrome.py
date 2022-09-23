class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        news=''


        for i in s:
            if ord(i)>=97 and ord(i)<=122:
                news+=i
            elif ord(i)>=65 and ord(i)<=90:
                news+=i
            elif ord(i)>=48 and ord(i)<=57:
                news+=i 


        news=news.lower()

        return news==news[::-1]
