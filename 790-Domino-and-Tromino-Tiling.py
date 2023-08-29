class Solution:
    def numTilings(self, n: int) -> int:
        # a_n = 2*a_(n-1) + a_(n-3)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        
        a, b, c = 1, 2, 5
        for i in range(4, n+1):
            a, b, c = b, c, (2*c+a) % (10**9 + 7)
        return c 
