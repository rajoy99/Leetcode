class LRUCache:

    def __init__(self, capacity: int):
        self.dic={}
        self.capacity=capacity
        self.q=collections.deque([])
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.dic[key]
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            self.q.remove(key)
        elif len(self.q)==self.capacity:
            v=self.q.popleft()
            self.dic.pop(v)
        self.dic[key]=value
        self.q.append(key)
            
     
        
        
