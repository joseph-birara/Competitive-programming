class MinStack:

    def __init__(self):
        self._stack1 = []
        self.mi = []
        

    def push(self, val: int) -> None:
        self._stack1.append(val)
        if self.mi:
            self.mi.append(min(self.mi[-1],val))
        else:
            self.mi.append(val)
            
        

    def pop(self) -> None:
        if self._stack1:
            self._stack1.pop()
            self.mi.pop()
            
        
        
        

    def top(self) -> int:
        if self._stack1:
            return  self._stack1[-1]
        
        

    def getMin(self) -> int:
        if self.mi:
            return self.mi[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()