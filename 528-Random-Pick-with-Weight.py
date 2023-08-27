class Solution:

    # def __init__(self, w: List[int]):
    #     self.w = w
    #     for i in range(1, len(w)):
    #         self.w[i] += self.w[i-1] 
    #     #print(self.w)
        
    # def pickIndex(self) -> int:
    #     p = random.randint(1,self.w[-1])
    #     for i in range(len(self.w)):
    #         if p <= self.w[i]:
    #             return i
        
    ## BINARY SEARCH
    def __init__(self, w: List[int]):
        self.w = w
        s = sum(w)
        self.w[0] = self.w[0]/s 
        for i in range(1, len(w)):
            self.w[i] = self.w[i-1] + self.w[i] / s

        # s = sum(w)
        # w[0] = w[0]/s 
        # for i in range(1, len(w)):
        #     w[i] = w[i-1] + w[i] / s
        # self.w = w

    def pickIndex(self) -> int:
        p = random.random()
        l, r = 0, len(self.w) - 1

        while l < r:
            m = (l+r) // 2
            if self.w[m] > p:
                r = m
            elif self.w[m] <= p:
                l = m + 1
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
