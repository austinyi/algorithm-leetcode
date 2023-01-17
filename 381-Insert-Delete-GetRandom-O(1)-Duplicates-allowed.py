class RandomizedCollection:

    def __init__(self):
        self.h = {}
        self.arr = []
        self.l = 0
        
    def insert(self, val: int) -> bool:
        if self.h.get(val, None) is not None:
            self.h[val] += [self.l]
            self.arr.append(val)
            self.l += 1
            return False
        else:
            self.h[val] = [self.l]
            self.arr.append(val)
            self.l += 1
            return True

    def remove(self, val: int) -> bool:
        if self.h.get(val, None) is None:
            return False
        
        temp = self.h[val][-1]
        self.arr[temp] = self.arr[-1]

        self.h[self.arr[-1]].remove(self.l - 1)
        self.h[self.arr[-1]].append(temp)
        
        if len(self.h[val]) == 1:
            self.h.pop(val)
        else:
            self.h[val].pop()

        self.arr.pop()
        self.l -= 1

        return True
        

    def getRandom(self) -> int:
        idx = random.randint(0, self.l - 1)
        return self.arr[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom
