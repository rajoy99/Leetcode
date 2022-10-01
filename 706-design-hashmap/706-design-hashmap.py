class MyHashMap:

    def __init__(self):
        self.entries=[]
        

    def put(self, key: int, value: int) -> None:
        
        for k,v in self.entries:
            if k==key:
                self.entries.remove((key,v))
                self.entries.append((key,value))
                return
        
        self.entries.append((key,value))
        
        

    def get(self, key: int) -> int:
        
        for k,v in self.entries:
            if k==key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        
        for k,v in self.entries:
            if k==key:
                self.entries.remove((key,v))
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)