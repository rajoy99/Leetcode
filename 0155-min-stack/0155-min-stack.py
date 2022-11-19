class MinStack:

    def __init__(self):
        self.stk=[]
        self.curmin=math.inf
        

    def push(self, val: int) -> None:
        if val<self.curmin:
            self.curmin=val
        self.stk.append(val)
            
        

    def pop(self) -> None:
        popped=self.stk.pop()
        if popped==self.curmin:
            if self.stk:
                self.curmin=min(self.stk)
            else:
                self.curmin=math.inf
            
        

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.curmin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()