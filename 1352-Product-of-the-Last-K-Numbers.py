class ProductOfNumbers:
    def __init__(self):
        self.prod = [1]

    def add(self, a):
        if a == 0:
            self.prod = [1]
        else:
            self.prod.append(self.prod[-1] * a)

    def getProduct(self, k):
        if k >= len(self.prod): 
            return 0
        return int(self.prod[-1] / self.prod[-k-1])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
