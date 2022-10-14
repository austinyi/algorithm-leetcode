class MyQueue:

    def __init__(self):
        self.ord = []
        self.inv = []

    def push(self, x: int) -> None:
        self.ord.append(x)

    def pop(self) -> int:
        if self.inv:
            return self.inv.pop()
        else:
            while self.ord:
                self.inv.append(self.ord.pop())
            return self.inv.pop()
    
    def peek(self) -> int:
        if self.inv:
            return self.inv[-1]
        else:
            while self.ord:
                self.inv.append(self.ord.pop())
            return self.inv[-1]

    def empty(self) -> bool:
        return not self.ord and not self.inv


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
