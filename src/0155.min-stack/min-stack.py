class MinStack:
    
    def __init__(self):
        self.stack = []
        self.mins = 0
        
    def push(self, x: int) -> None:
        if not self.stack:
            self.mins = x
            self.stack.append(0)
        else:
            compare = x - self.mins
            self.stack.append(compare)
            self.mins = x if compare < 0 else self.mins            

    def pop(self) -> None:
        top1 = self.stack.pop()
        if top1 < 0:
            self.mins = self.mins - top1

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.mins + self.stack[-1]
        else:
            return self.mins

    def getMin(self) -> int:
        return self.mins


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()