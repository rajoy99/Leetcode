class Solution:
    def validIPAddress(self, IP: str) -> str:
        s=''
        for i in IP:
            if i=='.':
                s=IP.split('.')
                break
            elif i==':':
                s=IP.split(':')
                for i in range(len(s)):
                    s[i]=s[i].lower()
                break
                
        if len(s)==0:
            return "Neither"
        
        def ipv4(s):
              
            for i in s:
                if not i.isnumeric():
                    return False
                if len(i)>1 and i[0]=='0':
                    return False
                if int(i)>255:
                    return False
                
                
            return True
        # for checking validity ipv6
        def is_hex(s):
            digits = set("0123456789abcdef")
            for char in s:
                if not (char in digits):
                    return False
            return True 
        
        
        def ipv6(s):
            
            for i in s:
                if len(i)>4 or len(i)==0:
                    return False
                if  not is_hex(i):
                    return False
                    
                    
            return True
        
        if len(s)==4 and ipv4(s):
            return "IPv4"
        elif len(s)==8 and ipv6(s):
            return "IPv6"
        else:
            return "Neither"
                
                
            
        
