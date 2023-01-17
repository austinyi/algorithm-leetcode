class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.arr = []
        self.l = 0
        
    def insert(self, val: int) -> bool:
        if self.h.get(val, None) is not None:
            return False
        self.arr.append(val)
        self.h[val] = self.l
        self.l += 1
        return True

    def remove(self, val: int) -> bool:
        if self.h.get(val, None) is None:
            return False

        self.arr[self.h[val]] = self.arr[-1]
        self.h[self.arr[-1]] = self.h[val]
        self.h.pop(val)
        self.arr.pop()
        self.l -= 1
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, self.l - 1)
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
