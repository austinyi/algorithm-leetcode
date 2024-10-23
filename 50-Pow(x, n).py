class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        
        if n % 2 == 0:
            t = self.myPow(x, n // 2)
            return t * t
        else:
            t = self.myPow(x, n // 2)
            return t * t * x
        
