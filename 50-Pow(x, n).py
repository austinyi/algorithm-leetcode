# 1: Binary (Recursive)
# time: O(logn), space: O(logn)
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
    
# 2: Binary (Iterative)
# time: O(logn), space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
                n -= 1
            elif n % 2 == 0:
                x *= x
                n //= 2
        return ans
